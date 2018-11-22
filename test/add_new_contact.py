from model.contact import Contact


def test1_add_group(app):
    # old_groups = app.group.count()
    # str = app.group.random_text_group()
    # Создание нового контакта
    app.contact.create(Contact(firstname = 'test', lastname = 'test', address = 'test'))
    # new_groups = app.group.count()
    # assert old_groups + 1 == new_groups