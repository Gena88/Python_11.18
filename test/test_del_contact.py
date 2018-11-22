from model.contact import Contact


def test1_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test', lastname='test', address='test',
                                   home_phone='123456', mobile_phone='123456', work_phone='123456',
                                   email='test', address2='test', phone2='123456'))
    # old_groups = app.group.count()
    app.contact.delete_first_contact()
    # new_groups = app.group.count()
    # assert old_groups - 1 == new_groups