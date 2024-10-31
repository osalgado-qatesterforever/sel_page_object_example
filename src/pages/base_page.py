from selenium import webdriver

class BasePage:
    driver = webdriver.Chrome()
    driver.implicitly_wait(1.0)

    def __int__(self):
        pass

    def get_page_title(self):
        return self.driver.title
