from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    """Класс описывает страницу корзины"""
    def click_continue_button(self):
        """Метод возвращает со страницы корзины в магазин"""
        self.driver.find_element(*CartPageLocators.CONTINUE_SHOP_BTN).click()

    def click_checkout_button(self):
        """Метод кликает по кнопке для перехода на страницу ввода информации"""
        self.driver.find_element(*CartPageLocators.CHECKOUT_BTN).click()

    def remove_product_from_cart(self):
        """Метод удаляет из корзины ранее добавленный товар
        Метод следует применять в тестах, где добавляется 1 товар, иначе assert будет показывать ошибку
        т.к. найдет в корзине 2 товар
        """
        if self.is_element_present(*CartPageLocators.CART_ITEM):
            self.driver.find_element(*CartPageLocators.REMOVE_BTN_IN_CART).click()
        assert not self.is_element_present(*CartPageLocators.CART_ITEM), "Кнопка 'Remove' не работает, товар не удален"
