from model.group import Group
from random import randrange

def test1_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.count()
    app.group.delete_first_group()
    new_groups = app.group.count()
    assert old_groups - 1 == new_groups



def test1_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.count()
    index = randrange(old_groups)
    app.group.delete_group_by_index(index)
    new_groups = app.group.count()
    assert old_groups - 1 == new_groups


# пробный тест по заполнению списка групп
# def test2_delete_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test'))
#     old_groups = app.group.get_group_list()
#     app.group.delete_first_group()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[0:1] = []
#     assert old_groups == new_groups