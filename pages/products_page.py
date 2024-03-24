from pages.base_page import BasePage
from pages.locators import ProductsPageLocators
from selenium.webdriver.support.select import Select


class ProductsPage(BasePage):
    """Класс описывает страницу выбора товаров"""

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
            assert sorted(price_list, reverse=True) == sort_list, f"{sorted(price_list)} != sort_list (По убыванию)"

    def add_and_check_remove_btn(self, rndm):
        """Метод проверяет появление кнопки 'Remove' в карточке товара после нажатия кнопки 'Add to cart' """
        self.add_to_cart_product(rndm)
        assert self.is_element_present(*ProductsPageLocators.REMOVE_BTN), \
            "После добавления товара кнопка 'Remove' не появилась"

    def click_remove_btn(self):
        self.driver.find_element(*ProductsPageLocators.REMOVE_BTN).click()

    def click_cart_link(self):
        """Метод кликает по ссылке на корзину и переходит в нее"""
        self.driver.find_element(*ProductsPageLocators.SHOPPING_CART_LINK).click()

    def save_attr_product(self, rndm):
        """Метод сохраняет аттрибуты товара (название, описание, цену) на странице магазина для дальнейшего сравнения"""
        attr_list = list()
        attr_list.append(self.driver.find_elements(*ProductsPageLocators.PRODUCT_NAME)[rndm].text)
        attr_list.append(self.driver.find_elements(*ProductsPageLocators.PRODUCT_DESCRIPTION)[rndm].text)
        attr_list.append(self.driver.find_elements(*ProductsPageLocators.PRODUCT_PRICE)[rndm].text)
        return attr_list

    def add_to_cart_product(self, rndm):
        """Метод добавления товара в корзину"""
        self.driver.find_elements(*ProductsPageLocators.ADD_TO_CART_BTN)[rndm].click()
