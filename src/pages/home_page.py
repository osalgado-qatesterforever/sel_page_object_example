from base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def get_url(self, url):
        self.driver.get(url)

    def click_login_button(self):
        login_button_xpath = \
            "//button[@class='button Button tertiary-alt compact headerMenuButton']//span[contains(text(),'Log In')]"
        login_button = self.driver.find_element(by=By.XPATH, value=login_button_xpath)
        login_button.click()

    def enter_email(self, email):
        email_xpath = "//input[@placeholder='Email']"
        email_field = self.driver.find_element(by=By.XPATH, value=email_xpath)
        email_field.send_keys(email)

    def click_cont_with_email(self):
        cont_with_email_xpath = "//span[normalize-space()='Continue with Email']"
        continue_with_email = self.driver.find_element(by=By.XPATH, value=cont_with_email_xpath)
        continue_with_email.click()

    def click_sign_in_with_email(self):
        sign_in_w_email_xpath = "//span[normalize-space()='Sign in with email instead']"
        sign_in_with_email = self.driver.find_element(by=By.XPATH, value=sign_in_w_email_xpath)
        sign_in_with_email.click()

    def enter_password(self, password):
        password_field = self.driver.find_element(by=By.NAME, value="passwordInput")
        password_field.send_keys(password)

    def click_second_sign_in_with_email(self):
        sign_in_w_email_xpath = "//span[normalize-space()='Continue with Email']"
        sign_in_with_email = self.driver.find_element(by=By.XPATH, value=sign_in_w_email_xpath)
        sign_in_with_email.click()

