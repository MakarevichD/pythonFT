import re

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("//index.php") and len(wd.find_elements_by_name('Delete')) > 0):
            wd.find_element_by_xpath("//a[@href='./']").click()

    def add_new_contact(self, contacts):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contacts)
        wd.find_element_by_xpath("//input[@value='Enter']").click()
        self.return_to_homepage()
        self.contact_cache = None

    def fill_contact_form(self,contacts):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.contact_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contacts.contact_middle)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.contact_surname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.contact_nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.contact_company)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.contact_title)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contacts.contact_address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.contact_email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contacts.contact_email_2)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contacts.home_num)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mobile_num)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contacts.work_num)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contacts.fax_num)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@onclick = 'DeleteSel()']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.edit_contact_by_index(0)

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("// *[@id = 'MassCB']").click()
        wd.find_element_by_xpath("//input[@onclick = 'DeleteSel()']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_contact_by_index(self, index, contacts):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()
        self.fill_contact_form(contacts)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_contact(self):
        self.edit_contact_by_index(0)

    def contacts_count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                contact_surname = cells[1].text
                contact_name = cells[2].text
                contact_address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(contact_name=contact_name, contact_surname=contact_surname,
                                                  all_phones_from_home_page=all_phones,all_emails_from_home_page = all_emails,
                                                  contact_address=contact_address, id=id,))

        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        contact_name = wd.find_element_by_name("firstname").get_attribute("value")
        contact_surname = wd.find_element_by_name("lastname").get_attribute("value")
        contact_middle = wd.find_element_by_name("middlename").get_attribute("value")
        contact_nickname =  wd.find_element_by_name("nickname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_num = wd.find_element_by_name("home").get_attribute("value")
        work_num = wd.find_element_by_name("work").get_attribute("value")
        mobile_num = wd.find_element_by_name("mobile").get_attribute("value")
        fax_num = wd.find_element_by_name("fax").get_attribute("value")
        address_data = wd.find_element_by_name("address").get_attribute("value")
        email_data = wd.find_element_by_name("email").get_attribute("value")
        email2_data = wd.find_element_by_name("email2").get_attribute("value")

        return Contact(id=id, mobile_num=mobile_num, work_num=work_num,
                       home_num=home_num, contact_name=contact_name, contact_surname=contact_surname,
                       contact_address=address_data,contact_email=email_data, contact_email_2=email2_data)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_num = re.search("H: (.*)", text).group(1)
        work_num = re.search("W: (.*)", text).group(1)
        mobile_num = re.search("M: (.*)", text).group(1)
        return Contact(id=id, mobile_num=mobile_num, work_num=work_num, home_num=home_num)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.app.wd.quit()
