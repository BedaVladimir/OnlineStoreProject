from pages.cart_page import CartPage
from pages.info_user_page import InfoUserPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from faker import Faker
import pytest


@pytest.mark.negative
def test_filling_user_info_without_lastname(driver):
    """Тест появления сообщения с ошибкой о незаполенном поле 'Last name'
    В тест передаются перменные со случайными тестовыми значениями: fname, lname, postcode"""
    fake = Faker()
    fname, postcode = fake.first_name(), fake.postcode()
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    product_page = ProductsPage(driver, driver.current_url)
    product_page.click_cart_link()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.click_checkout_button()
    info_page = InfoUserPage(driver, driver.current_url)
    info_page.fill_in_user_info(fname=fname, lname="", zipcode=postcode)
    info_page.click_continue_btn_in_infopage()
    info_page.get_user_info_error_msg("Error: Last Name is required")
