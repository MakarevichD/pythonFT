from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser, base_url):
        if browser== "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")
            self.wd = webdriver.Chrome(options=options)
        elif browser == "firefox":
            self.wd =webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_homepage(self):
        wd = self.wd
        if not wd.current_url.endswith("/addressbook"):
            wd.get(self.base_url)
            return wd

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
