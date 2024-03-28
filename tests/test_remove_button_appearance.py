from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import random
import pytest


@pytest.mark.regression
def test_remove_button_appearance(driver):
    """Тест проверяет появление кнопки 'Remove' после нажатия кнопки 'Add to cart'
    В тест передается переменная rndm для выбора случайного товара из списка"""
    rndm = random.randint(0, 5)
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    product_page = ProductsPage(driver, driver.current_url)
    product_page.add_and_check_remove_btn(rndm)
