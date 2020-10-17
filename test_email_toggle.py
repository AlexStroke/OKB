# -*- coding: utf-8 -*-
from user import User
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_email_toggle(app):
    app.login(User(mobile=791, password=""))
    app.open_profile_page()
    app.click_email_toggle()
    app.logout()

def tearDown(self):
    self.app.destroy()
