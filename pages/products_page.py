from pages.base_page import BasePage
from pages.locators import ProductsPageLocators
from selenium.webdriver.support.select import Select
import random


class ProductsPage(BasePage):
    """Класс описывает страницу выбора товаров"""
    def check_title_page_products(self):
        """Метод проверяет заголовок на странице товаров"""
        title = self.driver.find_element(*ProductsPageLocators.PAGE_TITLE).text
        assert title == "Products", "Заголовок на странице товаров должен быть Products"

    def select_sort_filter(self, *, value):
        """Метод проверяет сортировку товаров по цене
        варианты переменной value:
        lohi - Price (low to high)
        hilo - Price (high to low)"""
        price_list = []
        prices = self.driver.find_elements(*ProductsPageLocators.PRODUCT_PRICE)
        for i in prices:
            price_list.append(float(i.text[1:]))  # сохраняем не сорт. список в виде чисел без знака '$'
        dropdown = self.driver.find_element(*ProductsPageLocators.SORT_SELECTOR)
        Select(dropdown).select_by_value(value)
        # сохранение в новый список отсортированные цены
        sort_list = []
        prices_sort = self.driver.find_elements(*ProductsPageLocators.PRODUCT_PRICE)
        for i in prices_sort:
            sort_list.append(float(i.text[1:]))  # сохраняем сорт. список в виде чисел без знака '$'
        if value == "lohi":
            assert sorted(price_list) == sort_list, f"{sorted(price_list)} != sort_list (По возрастанию)"
        if value == "hilo":
            assert sorted(price_list, reverse=True) == sort_list, f"{sorted(price_list)} != sort_list(По убыванию)"

    def add_and_remove_product(self):
        """Метод проверяет появление кнопки 'Remove' в карточке товара после нажатия кнопки 'Add to cart' """
        rndm = random.randint(0, 5)  # рандомное число от 0 до 5, которое нужно для выбора случайного товара из 6
        product_name = self.driver.find_elements(*ProductsPageLocators.PRODUCT_NAME)[rndm].text
        self.driver.find_elements(*ProductsPageLocators.ADD_TO_CART_BTN)[rndm].click()
        assert self.is_element_present(*ProductsPageLocators.REMOVE_BTN), \
            "После добавления товара кнопка 'Remove' не появилась"
        print(product_name, rndm)
