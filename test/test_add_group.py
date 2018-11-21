# -*- coding: utf-8 -*-
from model.group import Group

def test1_add_group(app):
    app.group.create(Group(name='n_test', header='h_test', footer='f_test'))


def test2_add_empty_group(app):
    app.group.create(Group(name='test', header='header', footer='footer'))
