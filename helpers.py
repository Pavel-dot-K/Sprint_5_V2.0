from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators_module.Locators import Locators
import pytest
import random
import string

# Функция для заполнения логина, пароля и нажатия на кнопку Войти

def perform_login(driver, email="kandybin_31@gmail.com", password="543216"):
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
    email_input.clear()
    email_input.send_keys(email)

    password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
    password_input.clear()
    password_input.send_keys(password)
    wait.until(EC.element_to_be_clickable(Locators.ENTER_BUTTON)).click()

# Функция для проверки появления кнопки Оформить Заказ

def check_order_button_visible(driver):
    wait = WebDriverWait(driver, 10)
    try:
        order_button = wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert order_button.text == "Оформить заказ"
        return order_button
    except TimeoutException:
        pytest.fail("Кнопка 'Оформить заказ' не найдена или не видна")

# Функция для проверки появления текста Собери Бургер

def assert_constructor_text(driver, expected_text="Соберите бургер", timeout=10):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_TEXT))
    actual_text = element.text
    assert expected_text in actual_text, f"Ожидали '{expected_text}', получили: {actual_text}"
    
# Функция для рандоиной генирации Имени

def generate_random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Функция для рандомной генирации Логина

def generate_random_email(domain="example.com", length=8):
    chars = string.ascii_lowercase + string.digits
    local_part = ''.join(random.choice(chars) for _ in range(length))
    return f"{local_part}@{domain}"

# Функция для рандомной генирации Пароля

def generate_random_password(length=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(chars) for _ in range(length))

# Функция для проверки появления текста Войти

def check_login_header(wait, locator):
    try:
        element = wait.until(EC.presence_of_element_located(locator))
        if element.text == "Вход":
            return True
        else:
            print(f"Текст заголовка не совпадает: ожидается 'Вход', найдено '{element.text}'")
            return False
    except TimeoutException:
        print("Элемент заголовка входа не найден в течение времени ожидания")
        return False
    