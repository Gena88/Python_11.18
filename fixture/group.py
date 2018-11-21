


class GroupHelper:

    def __init__(self, app):
        self.app = app


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
        self.select_first_group(wd)
        # Удалить выбранную группу
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def select_first_group(self, wd):
        # Выбрать первую группу
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




    def open_group_page(self):
        wd = self.app.wd
        # Переход на страницу Group
        wd.find_element_by_link_text("groups").click()