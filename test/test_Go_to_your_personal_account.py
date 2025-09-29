# Проверка перехода в Личный Кабинет Go_to_your_personal_account.py


import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators_module.Locators import Locators

def test_login_and_personal_account(driver, login):
    wait = WebDriverWait(driver, 10)
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Клик по кнопке "Войти в аккаунт"
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

    # Вызов фикстуры для входа
    login()

    # Нажать на ссылку "Личный Кабинет"
    
    wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

    # Проверка текста в личном кабинете
    element = wait.until(EC.visibility_of_element_located(Locators.ACCOUNT_TEXT))
    expected_text = "В этом разделе вы можете изменить свои персональные данные"
    assert expected_text in element.text, f"Ожидался текст '{expected_text}', но получено: {element.text}"