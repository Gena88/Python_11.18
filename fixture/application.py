from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.group = GroupHelper(self)

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