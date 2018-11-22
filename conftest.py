import pytest
from fixture.application import Application


@pytest.fixture(scope = 'session')
def app(request):
    browser = request.config.getoption("--browser")
    fixture = Application(browser=browser)
    fixture.open_houme_page()
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
