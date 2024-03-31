from pages.base_page import BasePage
from pages.locators import UserInfoLocators
import allure


class InfoUserPage(BasePage):
    """Класс описывает страницу ввода информации покупателя"""

    def fill_in_user_info(self, /, fname, lname, zipcode):
        """Метод заполняет поля информации о покупателе
        параметры fname, lname, zipcode - будут передаваться при вызове функции в тесте
        Чтобы после этого метода был переход к дальнейшим действиям в тесте - нужно заполнить все 3 поля"""
        with allure.step("Заполнить поля информации о покупателе (имя, фамилия и почтовый индекс)"):
            self.driver.find_element(*UserInfoLocators.FIRST_NAME).send_keys(fname)
            self.driver.find_element(*UserInfoLocators.LAST_NAME).send_keys(lname)
            self.driver.find_element(*UserInfoLocators.ZIP_CODE).send_keys(zipcode)

    def get_user_info_error_msg(self, error_message):
        """Метод проверки наличия сообщения с ошибкой ввода данных
        Перед вызовом этого метода в тесте необходимо вызвать метод fill_in_user_info,
        где пустое поле First Name/ Last Name/ Postal Code
        Варианты переменной error_message для передачи в тесте:
        1. "Error: First Name is required" - переменная 'fname' в методе 'get_user_info_error_msg' пустая

        2. "Error: Last Name is required" - переменная 'lname' в методе 'get_user_info_error_msg' пустая

        3. "Error: Postal Code is required" - переменная 'zipcode' в методе 'get_user_info_error_msg' пустая"""
        with allure.step("Сравнить текст ошибки с образцом при заполнении информации без одного из полей"):
            error = self.driver.find_element(*UserInfoLocators.ERROR_MSG_TEXT)
            assert error.text == error_message, "Сообщение об ошибке не равно ошибке сделанной тестом"

    def click_cancel_button(self):
        """Метод проверяет работу кнопки 'Cancel' """
        with allure.step("Нажать на кнопку 'Cancel' на странице ввода информации о пользователе"):
            self.driver.find_element(*UserInfoLocators.CANCEL_BTN).click()

    def click_continue_btn_in_infopage(self):
        """ Метод проверяет работу кнопки 'Continue' на странице ввода информации пользователя"""
        with allure.step("Нажать на кнопку 'Continue' на странице ввода информации о пользователе"):
            self.driver.find_element(*UserInfoLocators.CONTINUE_BTN).click()
