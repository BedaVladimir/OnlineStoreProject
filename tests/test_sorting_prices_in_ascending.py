from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import pytest
import allure


@allure.title("Сортировка товаров по цене(по возрастанию)")
@pytest.mark.regression
def test_for_sorting_prices_in_ascending_order(driver):
    """Тест проверяет механизм сортировки товаров по цене(по возрастанию)"""
    page = LoginPage(driver, url="https://www.saucedemo.com/")
    page.open_url()
    page.auth(login="standard_user", password="secret_sauce")
    product_page = ProductsPage(driver, driver.current_url)
    product_page.select_sort_filter(value="lohi")
