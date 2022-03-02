from .pages.login_page import LoginPage

def test_guest_should_see_login_and_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


#Запуст теста
#pytest -v --tb=line --language=en test_login_page.py