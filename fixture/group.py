from model.group import Group
import random
import string

class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name("new")) > 0):
            # Переход на страницу Group
            wd.find_element_by_link_text("groups").click()


    def return_to_group_page(self):
        wd = self.app.wd
        # Переход на страницу Group
        wd.find_element_by_link_text("group page").click()


    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Инициализация добавления новой группы
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Сохранение введенных параметров
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        # Заполнение формы
        self.change_field_value('group_name', group.name)
        self.change_field_value('group_header', group.header)
        self.change_field_value('group_footer', group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        # Осуществляет проверку и если поле не пустое, то изменяет значение поля
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # Удалить выбранную группу
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()



    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # Удалить выбранную группу
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()


    def select_group_by_index(self, index):
        # Выбрать первую группу
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()



    def select_first_group(self):
        # Выбрать первую группу
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_date):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group(wd)
        # Модифицировать выбранную первую группу
        wd.find_element_by_name("edit").click()
        # Заполненеие формы
        self.fill_group_form(new_group_date)
        # Подтвердить корректировку
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))


    # Не удалось реализовать функцию по формированию списка груп, проверку реализовал с помощью функции COUNT
    # def get_group_list(self):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     spisok = []
    #     for element in wd.find_elements_by_css_selector('input[name="selected[]"]'):
    #         text = element.text
    #         id = element.find_element_by_xpath("/html/body/div/div/form/input").get_attribute('value')
    #         id = element.find_element_by_css_selector('input[name="selected[]"]').get_attribute('value')
    #         spisok.append(Group(id=id))
    #     return spisok


    def random_text_group(self):
        a = 'test_'
        b = ''.join([random.choice(string.digits) for i in range(4)])
        tg = a + b
        return tg




