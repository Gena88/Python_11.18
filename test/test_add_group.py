# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import random
import string


def random_string(prefix, maxlen=None):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i  in range(random.randrange(maxlen))])

testdata = [
    # Group(name=str, header=str, footer=str)
    Group(name=random_string("name", 5), header=random_string("header", 5), footer=random_string("footer", 5)),
    Group(name='', header='', footer='')
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test1_add_group(app, group):
    old_groups = app.group.count()
    # str = app.group.random_text_group()
    app.group.create(group)
    new_groups = app.group.count()
    assert old_groups + 1 == new_groups

# Пробный тест по заполнению списка групп
# def test1_1_add_group(app):
#     old_groups = app.group.get_group_list()
#     app.group.create(Group(name='n_test', header='h_test', footer='f_test'))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)



