from pages.cart_page import CartPage
from pages.info_user_page import InfoUserPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import pytest


@pytest.mark.regression
def test_press_button_cancel(driver):
    """Тест нажатия кнопки 'Cancel' на странице заполнения информации"""
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    product_page = ProductsPage(driver, driver.current_url)
    product_page.click_cart_link()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.click_checkout_button()
    info_page = InfoUserPage(driver, driver.current_url)
    info_page.click_cancel_button()
    info_page.check_title_page("Your Cart")
