from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.count()
    app.group.delete_first_group()
    new_groups = app.group.count()
    assert old_groups - 1 == new_groups
