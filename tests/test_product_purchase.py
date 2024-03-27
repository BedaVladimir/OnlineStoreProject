from pages.cart_page import CartPage
from pages.checkout_order_page import CheckoutPage
from pages.info_user_page import InfoUserPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import random
from faker import Faker


def test_for_calculating_the_sum_all_products(driver):
    """Тест считает сумму всех товаров и налог, после чего сравнивает с итогом на странице подтверждения
    В тест передается переменные rndm и для выбора случайного товара из списка
    В тест передаются переменные со случайными тестовыми значениями: fname, lname, postcode"""
    rndm = random.randint(0, 5)
    fake = Faker()
    fname, lname, postcode = fake.first_name(), fake.last_name(), fake.postcode()
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    product_page = ProductsPage(driver, driver.current_url)
    product_page.add_to_cart_product(rndm)
    product_page.click_cart_link()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.click_checkout_button()
    info_page = InfoUserPage(driver, driver.current_url)
    info_page.fill_in_user_info(fname=fname, lname=lname, zipcode=postcode)
    info_page.click_continue_btn_in_infopage()
    checkout_page = CheckoutPage(driver, driver.current_url)
    checkout_page.click_finish_button()
    checkout_page.check_complete_message()
