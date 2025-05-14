import allure

from ..locators.header import HeaderLocator


class HeaderPage:
    def __init__(self, browser):
        self.__browser = browser

    @allure.step("Нажимаем на логотип Yandex")
    def click_yandex_logo(self):
        button = self.__browser.find_element(*HeaderLocator.yandex)
        button.click()

    @allure.step("Нажимаем на логотип Самокат")
    def click_scooter_logo(self):
        button = self.__browser.find_element(*HeaderLocator.scooter)
        button.click()

    @allure.step("Нажимаем на кнопку Заказать")
    def click_order(self):
        button = self.__browser.find_element(*HeaderLocator.order)
        button.click()
