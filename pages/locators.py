from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") #селектор написан для проверки, что тест упадет при невалидном поиске
    BUTTON_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    INPUT_EMAIL = (By.ID, "id_registration-email")
    INPUT_PASSWORD_1 = (By.ID, "id_registration-password1")
    INPUT_PASSWORD_2 = (By.ID, "id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div:nth-child(3) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")

