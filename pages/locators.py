from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_SUCCESS_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div:nth-child(3) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")

