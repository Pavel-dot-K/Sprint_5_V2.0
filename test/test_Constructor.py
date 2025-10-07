import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators_module.Locators import Locators  # Подключаем локаторы

class TestConstructor:

    def test_navigate_to_buns_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait = WebDriverWait(driver, 10)
    
        # Кликаем по разделу Соусы
        wait.until(EC.element_to_be_clickable(Locators.SAUCES_SECTION)).click()
        # Кликаем по разделу Булки
        wait.until(EC.element_to_be_clickable(Locators.BUNS_SECTION)).click()

        # Проверяем, что раздел Булки отображается
        try:
            elem = wait.until(EC.presence_of_element_located(Locators.BUNS_TAB_FULL))
            assert elem.is_displayed(), "Раздел Булки не отображается"
        except TimeoutException:
            assert False, "Элемент раздела Булки не найден или не видим"

    def test_navigate_to_sauces_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait = WebDriverWait(driver, 10)

        # Кликаем по разделу Соусы
        wait.until(EC.element_to_be_clickable(Locators.SAUCES_SECTION)).click()

        # Проверяем, что раздел Соусы отображается
        try:
            elem = wait.until(EC.presence_of_element_located(Locators.SOUS_TAB_FULL))
            assert elem.is_displayed(), "Раздел Соусы не отображается"
        except TimeoutException:
            assert False, "Элемент раздела Соусы не найден или не видим"

    def test_navigate_to_fillings_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait = WebDriverWait(driver, 10)

        # Кликаем по разделу Начинки
        wait.until(EC.element_to_be_clickable(Locators.FILLINGS_SECTION)).click()

        # Проверяем, что раздел Начинки отображается
        try:
            elem = wait.until(EC.presence_of_element_located(Locators.FILLINGS_TAB_FULL))
            assert elem.is_displayed(), "Раздел Начинки не отображается"
        except TimeoutException:
            assert False, "Элемент раздела Начинки не найден или не видим"