from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException # требуется для получения ответа на задание https://stepik.org/lesson/201964/step/2?unit=176022
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators
import math



class BasePage():
    def __init__(self, browser, url, timeout=10): #Инициализация браузера
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout) #Явное ожидание, каждое действие будет ожидаться 10 секунд или выполняться моментально

    def open(self): #Открытие страницы
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url) #Можно в функции сразу вернуть новую инициализацию страницы, что бы не прописывать ее в тесте в ручную
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def is_element_present(self, how, what): #метод провери наличия елемента на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4): #метод для проверки отсутствия элемента на странице с явным ожиданием
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    # требуется для прохождения капчи в уроке https://stepik.org/lesson/201964/step/2?unit=176022
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        #time.sleep(5)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")




