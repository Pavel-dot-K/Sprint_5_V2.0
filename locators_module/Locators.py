from selenium.webdriver.common.by import By
class Locators:

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка Войти на главной странице

    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Текст-ссылка Зарегистрироваться

    NAME_INPUT = (By.XPATH, "//label[normalize-space(text())='Имя']/following-sibling::input")  # Поле ввода Имя

    EMAIL_INPUT = (By.XPATH, "//label[normalize-space(text())='Email']/following-sibling::input")  # Поле ввода Логина

    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space(text())='Пароль']/following-sibling::input")  # Поле ввода Пароля

    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space(text())='Зарегистрироваться']")  # Кнопка Зарегистрироваться

    ORDER_BUTTON = (By.XPATH, "//button[normalize-space(text())='Оформить заказ']")  # Кнопка Оформить заказ

    PERSONAL_ACCOUNT_LINK = (By.LINK_TEXT, "Личный Кабинет")  # Текст-ссылка Личный кабинет

    ENTER_BUTTON = (By.XPATH, "//button[normalize-space(text())='Войти']")  # Кнопка Войти

    RESTORE_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")  # Текст-ссылка Восстановить пароль

    RESTORE_PASSWORD_LOGIN_LINK = (By.LINK_TEXT, "Войти")  # Текст-ссылка Войти в форме Восстановления пароля

    REGISTRATION_FORM = (By.XPATH, "//div[contains(@class, 'Auth_login__3hAey') and h2[text()='Регистрация']]")  # Форма Регистрации 

    PASSWORD_ERROR_MESSAGE = (By.CLASS_NAME, "input__error")  # Текст ошибки для неверно введеного пароля

    CONSTRUCTOR_BUTTON = (By.CLASS_NAME, "AppHeader_header__link__3D_hX")  # текст-ссылка Конструктор

    CONSTRUCTOR_TEXT = (By.CLASS_NAME, "text_type_main-large")  # Текст Конструктор на главной странице

    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип StellarBurgers

    ACCOUNT_TEXT = (By.CLASS_NAME, "Account_text__fZAIn")  # Текст Мой Аккаунт в личном кабинете

    LOGOUT_BUTTON = (By.CLASS_NAME, "Account_button__14Yp3")  # Кнопка Выйти

    LOGIN_HEADER = (By.XPATH, "//h2[normalize-space(text())='Вход']")  # Кнопка Вход

    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # Текст-ссылка Войти в форме регистрации

    # Локатор для Булки

    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']")

    # Локатор для Соусы

    SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Соусы']")

    # Локатор для Начинки

    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Начинки']")

    # Локатор нажатой кнопки разела Соусы

    SOUS_TAB_FULL = (By.XPATH, '''
    //div[contains(@class, 'tab_tab__1SPyG') and 
        contains(@class, 'tab_tab_type_current__2BEPc') and
        contains(@class, 'pt-4') and 
        contains(@class, 'pr-10') and 
        contains(@class, 'pb-4') and 
        contains(@class, 'pl-10') and 
        contains(@class, 'noselect') 
        and span[text()="Соусы"]
    ]
''')
    
    # Локатор нажатой кнопки разела Булки

    BUNS_TAB_FULL = (By.XPATH, '''
    //div[
        contains(@class, 'tab_tab__1SPyG') and 
        contains(@class, 'tab_tab_type_current__2BEPc') and
        contains(@class, 'pt-4') and 
        contains(@class, 'pr-10') and 
        contains(@class, 'pb-4') and 
        contains(@class, 'pl-10') and 
        contains(@class, 'noselect')
        and span[text()="Булки"]
    ]
''')

    # Локатор нажатой кнопки разела Начинки

    FILLINGS_TAB_FULL = (By.XPATH, '''
    //div[contains(@class, 'tab_tab__1SPyG') and 
        contains(@class, 'tab_tab_type_current__2BEPc') and
        contains(@class, 'pt-4') and 
        contains(@class, 'pr-10') and 
        contains(@class, 'pb-4') and 
        contains(@class, 'pl-10') and 
        contains(@class, 'noselect') 
        and span[text()="Начинки"]
    ]
''')