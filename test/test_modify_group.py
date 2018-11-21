from model.group import Group

def test1_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.count()
    app.group.modify_first_group(Group(name="New_name"))
    new_groups = app.group.count()
    assert old_groups == new_groups

def test1_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.count()
    app.group.modify_first_group(Group(name="New_header"))
    new_groups = app.group.count()
    assert old_groups == new_groups