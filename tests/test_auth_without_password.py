from pages.login_page import LoginPage
import pytest


@pytest.mark.negative
def test_auth_without_password(driver):  # здесь метку негативного теста
    """Тест проверяет сценарий попытки авторизации без введенного пароля"""
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="")
    page.get_auth_error_msg(error_message="Epic sadface: Password is required")
