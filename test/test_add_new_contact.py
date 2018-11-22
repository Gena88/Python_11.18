from model.contact import Contact


def test1_add_group(app):
    # old_groups = app.group.count()
    # str = app.group.random_text_group()
    # Создание нового контакта
    app.contact.create(Contact(firstname = 'test', lastname = 'test', address = 'test',
                               home_phone = '123456', mobile_phone = '123456', work_phone = '123456',
                               email = 'test', address2 = 'test', phone2 = '123456'))
    # new_groups = app.group.count()
    # assert old_groups + 1 == new_groups