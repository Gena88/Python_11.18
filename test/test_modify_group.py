from model.group import Group

def test1_modify_group_name(app):
    app.group.modify_first_group(Group(name="New_name"))

def test1_modify_group_header(app):
    app.group.modify_first_group(Group(name="New_header"))