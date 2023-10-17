from unittest import TestCase
from home_page import HomePage


url = "https://www.redfin.com/"
email = "xxxxxx@gmail.com"
password = "xxxxxx"

class LoginPage(TestCase):

    def test_login(self):

        home_page = HomePage()
        home_page.get_url(url)
        home_page.click_login_button()
        home_page.enter_email(email)
        home_page.click_cont_with_email()
        home_page.click_sign_in_with_email()
        home_page.enter_password(password)
        home_page.click_second_sign_in_with_email()
        title = home_page.get_page_title()

        expected_title = "Real Estate, Homes for Sale, MLS Listings, Agents | Redfin"
        assert title == expected_title, f"expected title={expected_title}, got title={title}"
