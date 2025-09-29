import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators_module.Locators import Locators  # Подключаем локаторы

# Вспомогательная функция клика по разделу
def click_section(driver, locator):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(locator)).click()

# Вспомогательная функция проверки отображения раздела
def is_section_active(driver, locator):
    wait = WebDriverWait(driver, 10)
    try:
        elem = wait.until(EC.presence_of_element_located(locator))
        return elem.is_displayed()
    except TimeoutException:
        return False

# Общий хук для открытия страницы один раз для всех тестов
@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

# Проверяем переход в раздел Булки
def test_navigate_to_buns_section(driver):
    # Сначала кликаем по разделу Соусы
    click_section(driver, Locators.SAUCES_SECTION)
    # Затем кликаем по разделу Булки
    click_section(driver, Locators.BUNS_SECTION)
    assert is_section_active(driver, Locators.BUNS_SECTION)

# Проверяем переход в раздел Соусы
def test_navigate_to_sauces_section(driver):
    click_section(driver, Locators.SAUCES_SECTION)
    assert is_section_active(driver, Locators.SAUCES_SECTION)

# Проверяем переход в раздел Начинки
def test_navigate_to_fillings_section(driver):
    click_section(driver, Locators.FILLINGS_SECTION)
    assert is_section_active(driver, Locators.FILLINGS_SECTION)