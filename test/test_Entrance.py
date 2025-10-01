# Группа тестов по входу зарегистрированного пользователя Entrance.py

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators_module.Locators import Locators 
from helpers import check_order_button_visible, perform_login

class TestEntrance:

    # Вход под зарегистрированным пользователем через Личный Кабинет

    def test_login(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/")
    
        # Нажать ссылку "Личный Кабинет"
    
        wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

        # Выполнить логин через фикстуру
        perform_login(driver)

        # Кнопки "Оформить заказ" доступна
        check_order_button_visible(driver)


    # Вход под зарегистрированным пользователем через кнопку войти в форме восстановления пароля

    def test_login_via_restore_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait = WebDriverWait(driver, 10)

        # Нажать кнопку "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        # Нажать ссылку "Восстановить пароль"
    
        wait.until(EC.element_to_be_clickable(Locators.RESTORE_PASSWORD_LINK)).click()

        # Нажать ссылку "Войти" для возврата к форме входа
    
        wait.until(EC.element_to_be_clickable(Locators.RESTORE_PASSWORD_LOGIN_LINK)).click()

        # Логин
        perform_login(driver)

        # Кнопки "Оформить заказ" доступна
        check_order_button_visible(driver)

    # Вход под зарегистрированным пользователем через кнопку войти в форме регистрации

    def test_login_via_registration_flow(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/")

        # 1. Нажать кнопку "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        # 2. Нажать ссылку "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()

        # 3. Нажать текст-ссылку "Войти" в форме регистрации
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_LINK)).click()

        # Логин
        perform_login(driver)

        # Кнопки "Оформить заказ" доступна
        check_order_button_visible(driver)


    # Вход под зарегистрированным пользователем кнопка войти в аккаунт

    def test_login_via_login_button(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажать кнопку "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    
        # Логин
        perform_login(driver)

        # Кнопки "Оформить заказ" доступна
        check_order_button_visible(driver)
