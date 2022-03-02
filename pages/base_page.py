from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # требуется для получения ответа на задание https://stepik.org/lesson/201964/step/2?unit=176022
import math
import time

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
        except NoSuchElementException:
            return False
        return True

    # требуется для получения ответа на задание https://stepik.org/lesson/201964/step/2?unit=176022
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




