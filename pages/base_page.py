from selenium.common.exceptions import NoSuchElementException
class BasePage():
    def __init__(self, browser, url, timeout=10): #Инициализация браузера
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout) #Явное ожидание, каждое действие будет ожидаться 10 секунд или выполняться моментально

    def open(self): #Открытие страницы
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False



