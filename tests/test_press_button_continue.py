from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import random


def test_click_button_continue(driver):
    """Тест проверяет переход на страницу выбора товаров после нажатия кнопки 'Continue shopping'
    В тест передается переменная rndm для выбора случайного товара из списка"""
    rndm = random.randint(0, 5)
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    product_page = ProductsPage(driver, driver.current_url)
    product_page.add_to_cart_product(rndm)
    product_page.click_cart_link()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.click_continue_button()
    cart_page.check_title_page(except_title="Products")
