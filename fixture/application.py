from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def return_to_group_page(self):
        wd = self.wd
        # Переход на страницу Group
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # Инициализация добавления новой группы
        wd.find_element_by_name("new").click()
        # Заполнение формы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Сохранение введенных параметров
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.wd
        # Переход на страницу Group
        wd.find_element_by_link_text("groups").click()

    def open_houme_page(self):
        wd = self.wd
        # Открытие главной страницы
        wd.get("http://localhost/")

    def destroy(self):
        self.wd.quit()