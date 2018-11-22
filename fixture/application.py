from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self, browser="firefox"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Выбран не верный браузер %s" % browser)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_houme_page(self):
        wd = self.wd
        # Открытие главной страницы
        wd.get("http://localhost/")

    def destroy(self):
        self.wd.quit()