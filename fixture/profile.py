
class ProfileHelper:

    def __init__(self, app):
        self.app = app

    def click_profile_button(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//div[@id='navbarCollapse']/links/ul/li[5]/a/div/span").click()
        driver.find_element_by_link_text(u"Профиль").click()