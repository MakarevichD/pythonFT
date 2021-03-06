class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contacts):
        wd = self.app.wd
        self.app.open_homepage()
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
        self.return_to_homepage()

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

    def contact_modificate(self,contacts):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_xpath("//img[@title = 'Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.contact_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.contact_surname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mobile_num)
        wd.find_element_by_xpath("//input[@name ='update']").click()
        self.app.open_homepage()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.app.wd.quit()
