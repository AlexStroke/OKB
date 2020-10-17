from selenium import webdriver

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome("/Users/User/Downloads/chromedriver")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def click_email_toggle(self):
        driver = self.driver
        driver.find_element_by_xpath("//label/span").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='navbarCollapse']/links/ul/li[5]/a/div/span").click()
        driver.find_element_by_link_text(u"Выйти").click()

    def open_profile_page(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='navbarCollapse']/links/ul/li[5]/a/div/span").click()
        driver.find_element_by_link_text(u"Профиль").click()

    def login(self, user):
        driver = self.driver
        driver.get("https://ucbreport.ru/account")
        driver.find_element_by_xpath("//app-button-esia/a/span").click()
        driver.find_element_by_id("mobileOrEmail").click()
        driver.find_element_by_xpath("//button[@id='loginByPwdButton']/span").click()
        driver.find_element_by_id("mobileOrEmail").clear()
        driver.find_element_by_id("mobileOrEmail").send_keys(user.mobile)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(user.password)
        driver.find_element_by_xpath("//button[@id='loginByPwdButton']/span").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("https://ucbreport.ru/")

    def destroy(self):
        self.driver.quit()