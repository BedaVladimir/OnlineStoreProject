from pages.login_page import LoginPage
import pytest


@pytest.mark.negative
def test_auth_with_wrong_data(driver):  # здесь метку негативного теста
    """Тест проверяет сценарий попытки авторизации с неправильно введенным логином или паролем"""
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="wrong_user", password="wrong password")
    page.get_auth_error_msg(error_message="Epic sadface: Username and password do not match any user in this service")
