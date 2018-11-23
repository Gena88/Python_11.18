import json
import os.path
import pytest
from fixture.application import Application

target = None

@pytest.fixture(scope = 'session')
def app(request):
    global target
    browser = request.config.getoption("--browser")
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
    if target is None:
        config_file_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file_dir) as config_file:
            target = json.load(config_file)
    fixture = Application(browser=browser)
    fixture.open_houme_page()
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
