from pages.base_page import BasePage
from pages.locators import AuthPageLocators
from pages.locators import ProductsPageLocators


class LoginPage(BasePage):
    """Класс описывает страницу авторизации в интернет магазине"""

    def auth(self, *, login, password):
        """Метод авторизации в интернет-магазине"""
        self.driver.find_element(*AuthPageLocators.LOGIN_INPUT).send_keys(login)
        self.driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()

    def get_auth_error_msg(self, error_message):
        """Метод проверки наличия сообщения с ошибкой авторизации
        Перед вызовом этого метода в тесте необходимо вызвать метод auth, где пустой логин/пароль/логин и пароль
        Варианты переменной error_message:
        1. Epic sadface: Username is required - переменная login в методе 'auth' пустая
        2. Epic sadface: Password is required - переменная password пустая методе 'auth' пустая
        3. Epic sadface: Username and password do not match any user in this service - переменная login или password
        введены неправильно"""
        error = self.driver.find_element(*AuthPageLocators.ERROR_MESSAGE)
        assert error_message == error.text, "Сообщение об ошибке авторизации не соответствует ошибке сделанной тестом"
