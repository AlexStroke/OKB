from selenium import webdriver

from fixture.session import SessionHelper
from fixture.profile import ProfileHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome("/Users/User/Downloads/chromedriver")
        self.driver.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.profile = ProfileHelper(self)
        self.base_url = "https://www.google.com/"

    def click_email_toggle(self):
        driver = self.driver
        driver.find_element_by_xpath("//label/span").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("https://ucbreport.ru/")

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()