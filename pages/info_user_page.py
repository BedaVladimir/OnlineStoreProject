from pages.base_page import BasePage
from pages.locators import UserInfoLocators


class InfoUserPage(BasePage):
    """Класс описывает страницу ввода информации покупателя"""

    def fill_in_user_info(self, *, fname, lname, zipcode):
        """Метод заполняет поля информации о покупателе
        параметры fname, lname, zipcode - будут передаваться при вызове функции в тесте
        Чтобы после этого метода был переход к дальнейшим действиям в тесте - нужно заполнить все 3 поля
        """
        self.driver.find_element(*UserInfoLocators.FIRST_NAME).send_keys(fname)
        self.driver.find_element(*UserInfoLocators.LAST_NAME).send_keys(lname)
        self.driver.find_element(*UserInfoLocators.ZIP_CODE).send_keys(zipcode)
        self.driver.find_element(*UserInfoLocators.CONTINUE_BTN).click()

    def get_user_info_error_msg(self, error_message):
        """Метод проверки наличия сообщения с ошибкой ввода данных
        Перед вызовом этого метода в тесте необходимо вызвать метод fill_in_user_info,
        где пустое поле First Name/ Last Name/ Postal Code
        Варианты переменной error_message для передачи в тесте:
        1. "Error: First Name is required" - переменная 'fname' в методе 'get_user_info_error_msg' пустая

        2. "Error: Last Name is required" - переменная 'lname' в методе 'get_user_info_error_msg' пустая

        3. "Error: Postal Code is required" - переменная 'zipcode' в методе 'get_user_info_error_msg' пустая"""
        error = self.driver.find_element(*UserInfoLocators.ERROR_MSG_TEXT)
        assert error.text == error_message, "Сообщение об ошибке авторизации не соответствует ошибке сделанной тестом"

    def click_cancel_button(self):
        """Метод проверяет переход работу кнопки 'Cancel' """
        self.driver.find_element(*UserInfoLocators.CANCEL_BTN).click()
