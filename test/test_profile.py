# -*- coding: utf-8 -*-
from model.profile import Profile

def test_profile_button(app):
    app.profile.click_profile_button()
    assert app.session.get_url() == 'https://ucbreport.ru/cabinet'

#def test_mobile_phone(app):
    #app.profile.click_profile_button()
    #assert app.profile.get_mobile_from_page() == '79111153045'
