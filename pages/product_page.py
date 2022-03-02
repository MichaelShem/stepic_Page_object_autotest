from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    #реализация взаимодействия с продуктовой страницей и проверки
    def add_product_to_basket(self):
        #Добавляем товар
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_success_added(self):
        #Ищем название и стоимость товара
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        #Ищем алерт стоимости товара и стоимость корзины
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_PRODUCT_NAME).text
        alert_basket_total = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_TOTAL).text

        #Сравниваем сообщения с алерта с данными о товаре на странице
        assert product_name == alert_product_name, "invalid product name"
        assert product_price == alert_basket_total, "invalid basket total"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should disappeared, but did not"


