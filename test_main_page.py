import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage(): #объединили тесты в один класс и потетили меткой, для удобства запуска отдельных тестов
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                     # открываем страницу
        page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) #инициализируем новую страницу
        login_page.should_be_login_page() #Выполняем проверку, что перешли на страницу с логином

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_message_empty_basket()






#Запуст теста
#pytest -v --tb=line --language=en test_main_page.py
#Для запуска отдельного теста допишем метку: pytest -v -m login_guest --tb=line --language=en test_main_page.py