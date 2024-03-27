from pages.cart_page import CartPage
from pages.checkout_order_page import CheckoutPage
from pages.info_user_page import InfoUserPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from faker import Faker
import pytest


@pytest.mark.parametrize("list_products", [0, 1, 2, 3, 4, 5])  # список с индексами всех товаров на сайте
def test_product_attribute_comparison(driver, list_products):
    """Тест проверяет соответствие описания, цены и названия товара на всех страницах
    В тест передается переменные rndm и для выбора случайного товара из списка
    В тест передаются переменные со случайными тестовыми значениями: fname, lname, postcode"""
    fake = Faker()
    fname, lname, postcode = fake.first_name(), fake.last_name(), fake.postcode()
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    product_page = ProductsPage(driver, driver.current_url)
    # сохранение значений цены, описания, и названия товара на странице магазина в переменную
    product_page_attr = product_page.save_attr_product(list_products)
    product_page.add_to_cart_product(list_products)
    product_page.click_cart_link()
    cart_page = CartPage(driver, driver.current_url)
    # сохранение значений цены, описания, и названия товара на странице корзины в переменную
    cart_page_attr = cart_page.save_attr_product_in_cart()
    # сравнение значений цены, описания, названия товара со страниц магазина и корзины
    assert product_page_attr == cart_page_attr, \
        "Информация о товаре в корзине отличается от информации на странице магазина"
    cart_page.click_checkout_button()
    info_page = InfoUserPage(driver, driver.current_url)
    info_page.fill_in_user_info(fname=fname, lname=lname, zipcode=postcode)
    info_page.click_continue_btn_in_infopage()
    checkout_page = CheckoutPage(driver, driver.current_url)
    # сохранение значений цены, описания, и названия товара на странице подтверждения покупки в переменную
    checkout_page_attr = checkout_page.save_attr_product_in_check_page()
    assert cart_page_attr == checkout_page_attr, \
        "Информация о товаре в корзине отличается от информации на странице подтверждения покупки"
