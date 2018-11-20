# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test1_add_group(self):
        wd = self.wd
        self.open_houme_page(wd)
        self.open_group_page(wd)
        self.create_group(wd, Group(name='n_test', header='h_test', footer='f_test'))
        self.return_to_group_page(wd)

    def test2_add_empty_group(self):
        wd = self.wd
        self.open_houme_page(wd)
        self.open_group_page(wd)
        self.create_group(wd, Group(name='', header='', footer=''))
        self.return_to_group_page(wd)


    def return_to_group_page(self, wd):
        # Переход на страницу Group
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
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

    def open_group_page(self, wd):
        # Переход на страницу Group
        wd.find_element_by_link_text("groups").click()

    def open_houme_page(self, wd):
        # Открытие главной страницы
        wd.get("http://localhost/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
