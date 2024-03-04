from selenium.common.exceptions import NoSuchElementException
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
        """Метод для проверки нахождения элемента на странице"""
        try:
            self.driver.find_element(by, element)
        except NoSuchElementException:
            return False
        return True

    def check_title_page(self, /, by, element, except_title):
        """Метод проверяет заголовок на странице
         Метод нужен для подтверждения, что нажатие по кнопке осуществило переход юзера на правильную страницу
         by, element - передается значение локатора
         expect_title - передается строка с названием заголовка соответствующей страницы"""
        title = self.driver.find_element(by, element).text
        assert title == except_title, "Заголовок на странице должен быть - {title}"