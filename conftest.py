import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()