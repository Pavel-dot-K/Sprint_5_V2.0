# Группа тестов по регистрации пользователя Registration.py

import pytest
import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators_module.Locators import Locators



# Регистрация пользователя, с функцией генератор логина и пароля


def generate_random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_email(domain="example.com", length=8):
    chars = string.ascii_lowercase + string.digits
    local_part = ''.join(random.choice(chars) for _ in range(length))
    return f"{local_part}@{domain}"

def generate_random_password(length=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(chars) for _ in range(length))


def test_registration_flow_random(driver, verify_order_button):
    wait = WebDriverWait(driver, 10)
    driver.get("https://stellarburgers.nomoreparties.site/")

    name = generate_random_string(10)
    email = generate_random_email(length=12)
    password = generate_random_password(12)

    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

    wait.until(EC.visibility_of_element_located(Locators.NAME_INPUT)).send_keys(name)
    wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(email)
    wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT)).send_keys(password)

    wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
def check_login_header(wait):
    try:
        element = wait.until(EC.presence_of_element_located(Locators.LOGIN_HEADER))
        if element.text == "Вход":
            return True
        else:
            print(f"Текст заголовка не совпадает: ожидается 'Вход', найдено '{element.text}'")
            return False
    except TimeoutException:
        print("Элемент заголовка входа не найден в течение времени ожидания")
        return False



# Проверка регистрации с незаполненным полем Имя

def test_registration_form_remains(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

    email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
    email_input.send_keys("kandybin_31@gmail.com")

    password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
    password_input.send_keys("543216")

    wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()

    elements = driver.find_elements(*Locators.REGISTRATION_FORM)
    assert elements, "Форма регистрации не найдена или не отображается"
    assert any(e.is_displayed() for e in elements), "Форма регистрации не отображается"


# Проверка регистрации с паролем меньше шести символов и ошибки о некорректном пароле

def test_registration_password_error_message(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Клик по кнопке входа (главная страница)
    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login_button.click()

    # Нажать ссылку "Зарегистрироваться"
    register_link = wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK))
    register_link.click()

    # Заполнение поля "Имя"
    name_input = wait.until(EC.visibility_of_element_located(Locators.NAME_INPUT))
    name_input.send_keys("Kandybin_Pavel")

    # Заполнение поля "Email"
    email_input = wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
    email_input.send_keys("kandybin_31@gmail.com")

    # Заполнение поля "Пароль"
    password_input = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
    password_input.send_keys("54321")

    # Нажать кнопку "Зарегистрироваться"
    register_button = wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
    register_button.click()

    # Ожидание появления сообщения об ошибке
    error_message = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR_MESSAGE))

    # Проверка, что сообщение об ошибке не пустое и вывод в консоль
    error_text = error_message.text
    print(f"Сообщение об ошибке: {error_text}")
    assert error_text != "", "Ожидалось сообщение об ошибке, но оно не появилось."



# Проверка возможности регистрации нового пользователя

def test_registration_flow(driver, verify_order_button):
    wait = WebDriverWait(driver, 10)
    driver.get("https://stellarburgers.nomoreparties.site/")

    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

    wait.until(EC.visibility_of_element_located(Locators.NAME_INPUT)).send_keys("Pablo")
    wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys("kandybin_p_31@gmail.com")
    wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT)).send_keys("543216")

    wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
    verify_order_button()