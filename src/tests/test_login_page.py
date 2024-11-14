from src.pages.home_page import Homepage
from src.pages.sign_in_page import SignInPage


def test_login(desktop_web_driver):
    driver = desktop_web_driver  
    # email = os.environ.get("username")
    # password = os.environ.get("PASSWORD")
    username = "standard_user"
    password = "secret_sauce"
    home_page = Homepage(driver)

    sign_in_page = SignInPage(driver)
    sign_in_page.enter_username(username)
    sign_in_page.enter_password(password)
    sign_in_page.click_login()
    home_page.get_app_logo_text()