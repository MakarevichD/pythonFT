class GroupHelper:

    def __init__(self, app):
        self.app = app

    def group_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href = 'group.php']").click()
        wd.implicitly_wait(30)

    def creation(self, group):
        wd = self.app.wd
        self.group_page()
        wd.find_element_by_xpath("//input[@value = 'New group']").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value ='Delete group(s)']").click()
        self.return_to_group_page()

    def modify_group(self, group):
        wd = self.app.wd
        self.group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value ='Edit group']").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_xpath("//input[@value ='Update']").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
