from selenium.common.exceptions import NoSuchElementException
import allure
from pages.locators import BaseLocators


class BasePage:
    """Базовый класс"""

    def __init__(self, driver, url):
        """Инициализация браузера в базовом классе"""
        self.driver = driver
        self.url = url

    def open_url(self):
        """Метод для открытия страницы"""
        with allure.step("Перейти по ссылке"):
            self.driver.get(self.url)

    def is_element_present(self, by, element):
        """Метод для проверки нахождения элемента на странице"""
        with allure.step("Найти элемент на странице"):
            try:
                self.driver.find_element(by, element)
            except NoSuchElementException:
                return False
            return True

    def check_title_page(self, except_title):
        """Метод проверяет заголовок на странице
         Метод нужен для подтверждения, что нажатие по кнопке осуществило переход юзера на правильную страницу
         expect_title - передается строка с названием заголовка соответствующей страницы"""
        with allure.step(f"Найти на странице заголовок - {except_title}"):
            title = self.driver.find_element(*BaseLocators.TITLE).text
            assert title == except_title, f"Заголовок на странице должен быть - {title}"
