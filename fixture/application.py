from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        self.wd = webdriver.Chrome(options=options)
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()
        wd.implicitly_wait(120)

    def group_creation(self, group):
        wd = self.wd
        self.group_page()
        wd.find_element_by_name("new").click()
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

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def destroy(self):
        self.wd.quit()




