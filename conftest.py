import json
import os.path
import pytest
import importlib
from fixture.application import Application
from fixture.db import DbFixture

target = None

def load_config(file):
    global target
    if target is None:
        config_file_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file_dir) as config_file:
            target = json.load(config_file)
    return target

@pytest.fixture(scope = 'session')
def app(request):
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    fixture = Application(browser=browser)
    fixture.open_houme_page()
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


# def pytest_generate_tests(metafunc):
#     for fixture in metafunc.fixturenames:
#         if fixture.startswith("data_"):
#             testdata = load_form_module(fixture[5:])
#             metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
#
# def load_form_module(module):
#     importlib.import_module("data.%s" % module).testdata

@pytest.fixture(scope = 'session')
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'],)
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture