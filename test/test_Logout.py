# Проверка выхода из аккаунта кликом по кнопке «Выйти» в личном кабинете Logout.py


import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators_module.Locators import Locators

def test_login_and_logout(driver, login):
    wait = WebDriverWait(driver, 10)
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажать кнопку "Войти в аккаунт" 
    
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

    # Выполнить вход через фикстуру

    login()

    # Нажать на ссылку "Личный Кабинет"
    
    wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

    # Нажать на кнопку "Выйти"
    wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()

    # Проверить наличие заголовка "Вход" после выхода
    result = check_login_header(wait)
    print("Logout test result:", "PASSED" if result else "FAILED")
    assert result

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
