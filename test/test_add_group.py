# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test1_add_group(app):
    app.open_houme_page()
    app.create_group(Group(name='n_test', header='h_test', footer='f_test'))


def test2_add_empty_group(app):
    app.open_houme_page()
    app.create_group(Group(name='', header='', footer=''))
