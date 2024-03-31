from pages.login_page import LoginPage
import pytest
import allure


@allure.title("Попытка авторизации в системе с отсутствующим логином для входа")
@pytest.mark.negative
def test_auth_without_login(driver):
    """Тест проверяет сценарий попытки авторизации без введенного логина"""
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="", password="secret_sauce")
    page.get_auth_error_msg(error_message="Epic sadface: Username is required")
