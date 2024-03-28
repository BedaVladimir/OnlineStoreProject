from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import random
import pytest


@pytest.mark.regression
def test_click_button_checkout(driver):
    """Тест проверяет нажатие кнопки в корзине 'Checkout'
    В тест передается переменная rndm для выбора случайного товара из списка"""
    rndm = random.randint(0, 5)
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    product_page = ProductsPage(driver, driver.current_url)
    product_page.add_to_cart_product(rndm)
    product_page.click_cart_link()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.click_checkout_button()
    cart_page.check_title_page(except_title="Checkout: Your Information")
