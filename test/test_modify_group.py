from model.group import Group

def test1_modify_group_name(app):
    app.open_houme_page()
    app.group.modify_first_group(Group(name="New_name"))

# def test1_modify_group_header(app):
#     app.open_houme_page()
#     app.group.modify_first_group(Group(name="New_header"))