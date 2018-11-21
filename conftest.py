import pytest
from fixture.application import Application


@pytest.fixture(scope = 'session')
def app(request):
    fixture = Application()
    fixture.open_houme_page()
    request.addfinalizer(fixture.destroy)
    return fixture