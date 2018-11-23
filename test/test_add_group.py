# -*- coding: utf-8 -*-
import pytest

from data.groups import testdata

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test1_add_group(app, group):
    old_groups = app.group.count()
    app.group.create(group)
    new_groups = app.group.count()
    assert old_groups + 1 == new_groups


# def test2_add_group(app, data_groups):
#     group = data_groups
#     old_groups = app.group.count()
    # app.group.create(group)
    # new_groups = app.group.count()
    # assert old_groups + 1 == new_groups

# Пробный тест по заполнению списка групп
# def test1_1_add_group(app):
#     old_groups = app.group.get_group_list()
#     app.group.create(Group(name='n_test', header='h_test', footer='f_test'))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)



