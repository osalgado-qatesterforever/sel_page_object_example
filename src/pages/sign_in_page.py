from seleniumpagefactory.Pagefactory import PageFactory


class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    "username": ('ID', "user-name"),
    "password": ('XPATH', "//*[@data-test='password']"),
    "login": ('ID', "login-button")
    }

    def enter_username(self, username):
        self.username.set_text(username)

    def enter_password(self, password):
        self.password.set_text(password)

    def click_login(self):
        self.login.click()