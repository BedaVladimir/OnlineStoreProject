from pages.base_page import BasePage
from pages.locators import CartPageLocators, UserInfoLocators


class CartPage(BasePage):
    """Класс описывает страницу корзины"""

    def click_continue_button(self):
        """Метод возвращает со страницы корзины в магазин"""
        self.driver.find_element(*CartPageLocators.CONTINUE_SHOP_BTN).click()

    def click_checkout_button(self):
        """Метод кликает по кнопке для перехода на страницу ввода информации"""
        self.driver.find_element(*CartPageLocators.CHECKOUT_BTN).click()
        self.check_title_page(*UserInfoLocators.USER_INFO_TITLE, "Checkout: Your Information")

    def remove_product_from_cart(self):
        """Метод удаляет из корзины ранее добавленный товар. После удаления сравнивает 2 списка и проверяет,
        что товар удален со страницы корзины"""
        cart_item = self.driver.find_elements(*CartPageLocators.CART_ITEM)
        if len(cart_item) == 0:
            print("В корзине нет добавленных товаров")
        else:
            self.driver.find_element(*CartPageLocators.REMOVE_BTN_IN_CART).click()
            new_cart_item = self.driver.find_elements(*CartPageLocators.CART_ITEM)
            assert len(new_cart_item) == len(cart_item) - 1, "Кнопка 'Remove' не удалила товар со страницы корзины"

    def save_attr_product_in_cart(self):
        """Метод сохраняет аттрибуты товара товара (название, описание, цену) на странице корзины"""
        attr_list_cart = list()
        attr_list_cart.append(self.driver.find_element(*CartPageLocators.NAME_PRODUCT_IN_CART).text)
        attr_list_cart.append(self.driver.find_element(*CartPageLocators.DESC_PRODUCT_IN_CART).text)
        attr_list_cart.append(self.driver.find_element(*CartPageLocators.PRICE_PRODUCT_IN_CART).text)
        return attr_list_cart
