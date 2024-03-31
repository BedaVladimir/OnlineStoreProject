import pytest
import allure
from selenium import webdriver


@allure.title("Подготовка к тесту. Открытие браузера")
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
