# -*- coding: utf-8 -*-
from model.group import Group

def test1_add_group(app):
    app.open_houme_page()
    app.group.create(Group(name='n_test', header='h_test', footer='f_test'))


def test2_add_empty_group(app):
    app.open_houme_page()
    app.group.create(Group(name='', header='', footer=''))
