from seleniumpagefactory.Pagefactory import PageFactory


class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
     "app_logo": ("XPATH", "//div[contains(@class, 'app_logo')]"),
    }

    def get_app_logo_text(self):
        retrieved_app_logo_text = self.app_logo.get_text()
        expected_app_logo_text = "Swag Labs"
        msg = f"Expected app logo text {expected_app_logo_text}, but found: {retrieved_app_logo_text}"
        assert retrieved_app_logo_text == expected_app_logo_text, msg