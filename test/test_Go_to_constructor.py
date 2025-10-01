# Группа тестов на проверку перехода в конструктор из личного кабинета Go_to_constructor.py


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators_module.Locators import Locators
from helpers import assert_constructor_text, perform_login


class TestGoToConstructor:

    #  Переход из личного кабинета кликом на конструктор

    def test_login_and_constructor_access_from_account(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажать кнопку "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        # вызов функции для входа 
        perform_login(driver)

        # Перейти в Личный Кабинет
    
        wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

        # Найти и нажать кнопку Конструктор
    
        wait.until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()

        # Проверить, что отображается текст "Соберите бургер"
        assert_constructor_text(driver, "Соберите бургер")

    # Переход из личного кабинета в конструктор кликом по лого

    def test_login_and_constructor_via_logo(self, driver, login):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажать кнопку "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        # вызов функции для входа
        perform_login(driver)

        # Нажать на ссылку "Личный Кабинет"
    
        wait.until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_LINK)).click()

        # Нажать на логотип Stellar Burgers
        wait.until(EC.element_to_be_clickable(Locators.LOGO)).click()

        # Проверить, что отображается текст "Соберите бургер"
        assert_constructor_text(driver, "Соберите бургер")