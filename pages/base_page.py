from selenium.common.exceptions import NoSuchElementException
from pages.locators import AuthPageLocators
import datetime


class BasePage:
    """Базовый класс"""
    now_time = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M")

    def __init__(self, driver, url):
        """Инициализация браузера в базовом классе"""
        self.driver = driver
        self.url = url

    def open_url(self):
        """Метод для открытия страницы"""
        self.driver.get(self.url)

    def is_element_present(self, by, element):
        """Метод для  элемента на странице"""
        try:
            self.driver.find_element(by, element)
        except NoSuchElementException:
            return False
        return True

    def auth(self, *, login, password):
        """Метод авторизации в интернет-магазине"""
        self.driver.find_element(*AuthPageLocators.LOGIN_INPUT).send_keys(login)
        self.driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()

    def get_auth_error_msg(self, error_message):
        """Метод проверки наличия сообщения с ошибкой авторизации
        Варианты переменной error_message:
        1. Epic sadface: Username is required - переменная login в методе 'auth' пустая
        2. Epic sadface: Password is required - переменная password пустая методе 'auth' пустая
        3. Epic sadface: Username and password do not match any user in this service - переменная login или password
        введены неправильно"""
        error = self.driver.find_element(*AuthPageLocators.ERROR_MESSAGE)
        assert error.text == error_message, "Сообщение об ошибке авторизации не соответствует ошибке сделанной тестом"
