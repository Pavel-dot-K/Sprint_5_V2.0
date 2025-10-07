# Проверка выхода из аккаунта кликом по кнопке «Выйти» в личном кабинете Logout.py


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators_module.Locators import Locators
from helpers import perform_login, check_login_header

class TestLogout: 

    def test_login_and_logout(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажать кнопку "Войти в аккаунт" 
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        # Выполнить вход
        perform_login(driver)

        # Перейти в личный кабинет
        wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

        # Выйти из аккаунта
        wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()

        # Проверить наличие заголовка "Вход" после выхода
        result = check_login_header(wait, Locators.LOGIN_HEADER)

        if result:
            print("Выход выполнен успешно. Заголовок 'Вход' отображается.")
        else:
            print("Проверка не прошла. Заголовок 'Вход' не найден.")
        assert result

