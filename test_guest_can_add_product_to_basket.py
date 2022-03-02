from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                       # открываем страницу
    page.add_product_to_basket()      # Добавляем товар в корзину
    page.solve_quiz_and_get_code()    # Выполняем функцию по расчету задачи и закрытии алерта
    page.should_be_success_added()    # Проверяем, что товар успешно добавлен в корзину и общая стоимость корзины корректна


#Запуст теста
#pytest -v --tb=line --language=en test_guest_can_add_product_to_basket.py