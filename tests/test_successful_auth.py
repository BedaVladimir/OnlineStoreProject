from pages.login_page import LoginPage


def test_successful_auth(driver):  # метку смок тест
    """Тест проверяет сценарий авторизации в магазине"""
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    page.check_title_page(except_title="Products")
