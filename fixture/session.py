from model import profile

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def get_url(self):
        return self.app.driver.current_url

    def login(self, user):
        driver = self.app.driver
        if not driver.current_url.endswith("/account"):
            driver.get("https://ucbreport.ru/account")
        driver.find_element_by_xpath("//app-button-esia/a/span").click()
        driver.find_element_by_id("mobileOrEmail").click()
        driver.find_element_by_xpath("//button[@id='loginByPwdButton']/span").click()
        driver.find_element_by_id("mobileOrEmail").clear()
        driver.find_element_by_id("mobileOrEmail").send_keys(user.mobile)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(user.password)
        driver.find_element_by_xpath("//button[@id='loginByPwdButton']/span").click()

    def ensure_login(self, user):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(user.surnameNS):
                return
            else:
                self.logout()
        self.login(user)


    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//div[@id='navbarCollapse']/links/ul/li[5]/a/div/span").click()
        driver.find_element_by_link_text(u"Выйти").click()

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        driver.get("https://ucbreport.ru/account")
        return len(driver.find_elements_by_link_text("Выйти")) > 0

    def is_logged_in_as(self, surnameNS):
        driver = self.app.driver
        return driver.find_element_by_xpath("//*[@id='navbarCollapse']/links/ul/li[5]/a/div/span").text == surnameNS
