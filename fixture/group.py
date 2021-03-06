class GroupHelper:

    def __init__(self, app):
        self.app = app

    def group_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href = 'group.php']").click()
        wd.implicitly_wait(30)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def creation(self, group):
        wd = self.app.wd
        self.group_page()
        wd.find_element_by_xpath("//input[@value = 'New group']").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.group_page()
        self.select_first_group()
        wd.find_element_by_xpath("//input[@value ='Delete group(s)']").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.group_page()
        self.select_first_group()
        wd.find_element_by_xpath("//input[@value ='Edit group']").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_xpath("//input[@value ='Update']").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
