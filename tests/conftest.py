import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@allure.title("Подготовка к тесту. Открытие браузера")
@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
