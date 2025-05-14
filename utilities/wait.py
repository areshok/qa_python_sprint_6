import time
from selenium.common.exceptions import (
    ElementClickInterceptedException, NoSuchElementException)
import allure


class Wait:
    "Класс ожидания"
    TIME_MAX = 10

    @staticmethod
    @allure.step("Ожидание появление элемента")
    def element(browser, path):
        "Ожидание элемента"
        time_start = time.time()
        while True:
            try:
                element = browser.find_element(*path)
                return element
            except NoSuchElementException as e:
                if time.time() - time_start > Wait.TIME_MAX:
                    raise e
                time.sleep(0.5)

    @staticmethod
    @allure.step("Ожидание нажатия на кнопку")
    def click(browser, path=None, element=None):
        "Ожидание нажатия"
        time_start = time.time()
        if element is None:
            button = isinstance.element(browser, path)
        else:
            button = element
        while True:
            try:
                button.click()
                return button
            except ElementClickInterceptedException as e:
                if time.time() - time_start > Wait.TIME_MAX:
                    raise e
                time.sleep(0.5)
