from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        self.wd = webdriver.Chrome(options=options)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_homepage(self):
        wd = self.wd
        if not wd.current_url.endswith("/addressbook"):
            wd.get("http://localhost/addressbook")
            return wd

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
