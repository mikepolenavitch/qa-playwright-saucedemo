#Test login functionality

from pages.login_page import LoginPage

def test_standard_user_can_login(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )

    assert page.locator("[data-test='title']").inner_text() == "Products"