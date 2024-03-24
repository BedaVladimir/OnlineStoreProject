from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_for_sorting_prices_in_descending_order(driver):
    """Тест проверяет механизм сортировки товаров по цене(по убыванию)"""
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    product_page = ProductsPage(driver, driver.current_url)
    product_page.select_sort_filter(value="hilo")
