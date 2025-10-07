import pytest
from selenium import webdriver
from helpers import perform_login, check_order_button_visible, assert_constructor_text

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    def _login(email="kandybin_31@gmail.com", password="543216"):
        perform_login(driver, email, password)
    return _login

@pytest.fixture
def verify_order_button(driver):
    def _verify():
        return check_order_button_visible(driver)
    return _verify

@pytest.fixture
def assert_constructor_text_fixture(driver):
    def _assert(expected_text="Соберите бургер", timeout=10):
        assert_constructor_text(driver, expected_text, timeout)
    return _assert
