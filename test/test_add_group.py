# -*- coding: utf-8 -*-
from model.group import Group

def test1_add_group(app):
    old_groups = app.group.count()
    app.group.create(Group(name='n_test', header='h_test', footer='f_test'))
    new_groups = app.group.count()
    assert old_groups + 1 == new_groups

def test1_1_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name='n_test', header='h_test', footer='f_test'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test2_add_empty_group(app):
    old_groups = app.group.count()
    app.group.create(Group(name='test', header='header', footer='footer'))
    new_groups = app.group.count()
    assert old_groups + 1 == new_groups

