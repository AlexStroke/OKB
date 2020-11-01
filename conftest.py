import pytest
import json

from fixture.application import Application
from model.profile import Profile

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid(): #если фикстура не проинициализировалась или невалидна
        fixture = Application()
    fixture.session.ensure_login(Profile(mobile=target['mobile'], password=target['password']))
    return fixture

@pytest.fixture(scope="session", autouse = True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")