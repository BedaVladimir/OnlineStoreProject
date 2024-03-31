from pages.base_page import BasePage
from pages.locators import CheckoutPageLocators
import allure


class CheckoutPage(BasePage):
    """Класс описывает страницу покупки товара"""

    def check_sum_of_prices_all_products(self):
        """Проверка отображения правильной суммы всех товаров на странице оплаты"""
        with allure.step("Посчитать сумму цен за все товары и сравнить с отображемой на странице"):
            all_prices = self.driver.find_elements(*CheckoutPageLocators.PRICE_PRODUCT_CHECK)
            all_prices_float = [float(price.text[1:]) for price in all_prices]  # сохранение цены всех товаров в список
            # сохранение строки с суммой все товаров и выделение числа из строки
            item_total = self.driver.find_element(*CheckoutPageLocators.ITEM_TOTAL).text[13:]
            assert sum(all_prices_float) == float(item_total), \
                f"Cумма всех товаров ({sum(all_prices_float)}) != итоговой сумме на странице подтверждения оплаты " \
                f"({float(item_total)})"

    def check_total_price(self):
        """Метод считает сумму всех товаров + налог и сравнивает с итоговой ценой"""
        # сохранение строки с суммой все товаров и выделение числа из строки
        with allure.step("Посчитать сумму цен за все товары + налог и сравнить с отображемой на странице"):
            sum_all_prices = float(self.driver.find_element(*CheckoutPageLocators.ITEM_TOTAL).text[13:])
            # сохранение строки с налогом и выделение числа из строки
            tax = float(self.driver.find_element(*CheckoutPageLocators.TAX).text[6:])
            # сохранение строки с итоговой ценой и выделение числа из строки
            total_price = float(self.driver.find_element(*CheckoutPageLocators.TOTAL_PRICE).text[8:])
            assert (round(sum_all_prices + tax, 2)) == total_price, \
                f"Рассчитанная сумма всех цен + налог ({sum_all_prices + tax})" \
                f"не соответствует итоговой цене на странице ({total_price})"

    def click_finish_button(self):
        """Метод нажимает на кнопку 'Finish'. Завершение покупки"""
        with allure.step("Нажать на кнопку 'Finish' на странице подтверждения оплаты"):
            self.driver.find_element(*CheckoutPageLocators.FINISH_BUTTON).click()

    def check_complete_message(self):
        """Метод проводит проверку сообщения с благодарностью за покупку"""
        with allure.step("Сравнить сообщение о успешной покупке с образцом"):
            complete_txt = self.driver.find_element(*CheckoutPageLocators.COMPLETE_TEXT).text
            assert complete_txt == "Thank you for your order!", \
                "После завершения нет сообщения об успешной покупке / Текст сообщения отличается от образца"

    def save_attr_product_in_check_page(self):
        """Метод сохраняет аттрибуты товара товара (название, описание, цену) на странице подтверждения покупки"""
        with allure.step("Сохранить значения названия, описания и цены товара на странице покупки"):
            attr_list_check = list()
            attr_list_check.append(self.driver.find_element(*CheckoutPageLocators.NAME_PRODUCT_CHECK).text)
            attr_list_check.append(self.driver.find_element(*CheckoutPageLocators.DESC_PRODUCT_CHECK).text)
            attr_list_check.append(self.driver.find_element(*CheckoutPageLocators.PRICE_PRODUCT_CHECK).text)
            return attr_list_check
