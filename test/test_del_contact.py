from model.contact import Contact


def test1_delete_first_contact(app):
    # if app.group.count() == 0:
    #     app.group.create(Group(name='test'))
    # old_groups = app.group.count()
    app.contact.delete_first_contact()
    # new_groups = app.group.count()
    # assert old_groups - 1 == new_groups