from selenium import webdriver
from src.pages.home_page import Homepage
from src.pages.sign_in_page import SignInPage


def test_browserstack():
    driver = webdriver.Chrome()
    driver.get("https://bstackdemo.com/")

    home_page = Homepage(driver)
    sign_in_page = SignInPage(driver)

    home_page.click_sign_in()

    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()
    home_page.get_username()
    driver.quit()