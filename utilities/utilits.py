import datetime
import platform
from selenium.webdriver.common.keys import Keys
import allure

OS = platform.system()


class ClearField:
    "Класс для очиски поля в зависимости от системы"

    def __define_os(self, field):
        if OS == "Windows" or OS == "Linux":
            self.__clean_win_uix(field)
        if OS == "Darwin":
            self.__clean_mac_os(field)

    def __clean_mac_os(self, field):
        field.send_keys(Keys.COMMAND + "a")
        field.send_keys(Keys.DELETE)

    def __clean_win_uix(self, field):
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)

    def __call__(self, field):
        self.__define_os(field)


@allure.step("Получаем завтрашнюю дату")
def get_tomorrow_day():
    "Возвращяет завтрашную дату"
    return str((datetime.date.today() + datetime.timedelta(days=1)
                ).strftime("%d.%m.%Y"))


@allure.step("Прокрутка до элемента")
def scrol_for_element(browser, element):
    "Прокрукта до элемента"
    browser.execute_script("arguments[0].scrollIntoView();", element)
