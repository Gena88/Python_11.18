from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def open_add_new_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/edit.php') and len(wd.find_elements_by_name("submit")) > 0):
            # Переход на страницу Group
            wd.find_element_by_link_text("add new").click()



    def return_to_home_page(self):
        wd = self.app.wd
        # Переход на страницу Group
        wd.find_element_by_link_text("home page").click()


    # !!! Проблемы при запуске из функции delete_first_contact !!!
    # def open_houme_page(self):
    #     wd = self.wd
    #     Открытие главной страницы
        # wd.get("http://localhost/")



    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_contact_form(contact)
        # Сохранение введенных параметров
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()



    def fill_contact_form(self, contact):
        wd = self.app.wd
        # Заполнение формы
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('lastname', contact.lastname)
        self.change_field_value('address', contact.address)
        self.change_field_value('home', contact.home_phone)
        self.change_field_value('mobile', contact.mobile_phone)
        self.change_field_value('work', contact.work_phone)
        self.change_field_value('email', contact.address)
        self.change_field_value('address2', contact.address)
        self.change_field_value('phone2', contact.address)



    def change_field_value(self, field_name, text):
        wd = self.app.wd
        # Осуществляет проверку и если поле не пустое, то изменяет значение поля
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def delete_first_contact(self):
        wd = self.app.wd
        # !!! Проблемы при запуске функции open_houme_page !!!
        # self.open_houme_page()
        self.select_first_contact(wd)
        # Удалить выбранную группу
        wd.find_element_by_css_selector('input[value="Delete"').click()
        self.return_to_home_page()



    def select_first_contact(self, wd):
        # Выбрать первую группу
        wd.find_element_by_css_selector('img[title="Edit"').click()

