import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators_module.Locators import Locators 

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    def _login(email="kandybin_31@gmail.com", password="543216"):
        wait = WebDriverWait(driver, 10)
        email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

        password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        wait.until(EC.element_to_be_clickable(Locators.ENTER_BUTTON)).click()
    return _login

@pytest.fixture
def verify_order_button(driver):
    def _verify():
        wait = WebDriverWait(driver, 10)
        try:
            order_button = wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
            assert order_button.text == "Оформить заказ"
            return order_button
        except TimeoutException:
            pytest.fail("Кнопка 'Оформить заказ' не найдена или не видна")
    return _verify


@pytest.fixture
def assert_constructor_text(driver):
    def _assert_text(expected_text="Соберите бургер", timeout=10):
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TEXT))
        actual_text = element.text
        assert expected_text in actual_text, f"Ожидали '{expected_text}', получили: {actual_text}"
    return _assert_text