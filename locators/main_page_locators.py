from selenium.webdriver.common.by import By

class MainPageLocators:
    """Устойчивые локаторы для главной страницы Яндекс.Самокат.
       Локаторы FAQ привязаны к тексту вопроса, а не к хрупким ID."""

    # Кнопки заказа
    ORDER_BUTTON_UP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_DOWN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Логотипы
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Кнопка закрытия баннера куки
    COOKIE_BANNER_CLOSE_BUTTON = (By.ID, "rcc-confirm-button")
    # --- ЛОКАТОРЫ ДЛЯ FAQ "Вопросы о важном" (УСТОЙЧИВЫЕ) ---
    # Локаторы вопросов (по тексту)
    FAQ_QUESTION_COST = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Сколько это стоит?')]")
    FAQ_QUESTION_MULTIPLE_SCOOTERS = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Хочу сразу несколько самокатов!')]")
    FAQ_QUESTION_RENTAL_TIME = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Как рассчитывается время аренды?')]")
    FAQ_QUESTION_TODAY_ORDER = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Можно ли заказать самокат на сегодня?')]")
    FAQ_QUESTION_EXTEND_RENT = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Можно ли продлить заказ?')]")
    FAQ_QUESTION_CHARGING = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Вы привозите зарядку вместе с самокатом?')]")
    FAQ_QUESTION_CANCEL = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Можно ли отменить заказ?')]")
    FAQ_QUESTION_FAR_ZONE = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Я живу за МКАДом, привезёте?')]")

    # Локаторы ответов (находятся рядом с соответствующим вопросом)
    FAQ_ANSWER_COST = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Сколько это стоит?')]/following-sibling::div[contains(@class, 'accordion__panel')]")
    FAQ_ANSWER_MULTIPLE_SCOOTERS = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Хочу сразу несколько самокатов!')]/following-sibling::div[contains(@class, 'accordion__panel')]")
    FAQ_ANSWER_RENTAL_TIME = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Как рассчитывается время аренды?')]/following-sibling::div[contains(@class, 'accordion__panel')]")
    FAQ_ANSWER_TODAY_ORDER = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Можно ли заказать самокат на сегодня?')]/following-sibling::div[contains(@class, 'accordion__panel')]")
    FAQ_ANSWER_EXTEND_RENT = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Можно ли продлить заказ?')]/following-sibling::div[contains(@class, 'accordion__panel')]")
    FAQ_ANSWER_CHARGING = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Вы привозите зарядку вместе с самокатом?')]/following-sibling::div[contains(@class, 'accordion__panel')]")
    FAQ_ANSWER_CANCEL = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Можно ли отменить заказ?')]/following-sibling::div[contains(@class, 'accordion__panel')]")
    FAQ_ANSWER_FAR_ZONE = (By.XPATH, ".//div[contains(@class, 'accordion__heading') and contains(., 'Я живу за МКАДом, привезёте?')]/following-sibling::div[contains(@class, 'accordion__panel')]")