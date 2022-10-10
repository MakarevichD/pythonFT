class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contacts):
        wd = self.app.wd
        self.app.open_homepage()
        self.fill_contact_form(contacts)
        self.return_to_homepage()

    def fill_contact_form(self, contacts):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.contact_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.contact_surname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mobile_num)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contacts.work_num)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@onclick = 'DeleteSel()']").click()
        wd.switch_to.alert.accept()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_xpath("// *[ @ id = 'MassCB']").click()
        wd.find_element_by_xpath("//input[@onclick = 'DeleteSel()']").click()
        wd.switch_to.alert.accept()

    def contact_modificate(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title ='Edit']").click()
        self.app.fill_contact_form(contact)
        wd.find_element_by_name("Update]").click()

    def edit_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']//img[@title='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()

    def contacts_count(self):
        wd = self.app.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.app.wd.quit()
