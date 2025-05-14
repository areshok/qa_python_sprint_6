from selenium.webdriver.common.keys import Keys
import allure

from ..locators.order import PageOne, PageTwo, PageConfirm
from ..utilities.utilits import ClearField


class OrderPageOne:
    def __init__(self, browser):
        self.__browser = browser

    @allure.step("Заполняем поле Имя")
    def write_first_name(self, fname):
        field = self.__browser.find_element(*PageOne.first_name)
        field.send_keys(fname)

    @allure.step("Заполняем поле Фамилия")
    def write_last_name(self, lname):
        field = self.__browser.find_element(*PageOne.last_name)
        field.send_keys(lname)

    @allure.step("Заполняем поле Адрес")
    def write_address(self, address):
        field = self.__browser.find_element(*PageOne.address)
        field.send_keys(address)

    @allure.step("Выбираем станцию метро в поле Станция")
    def choise_metro_stantion(self, metro):
        update_xpath = PageOne.station[1].format(metro.strip())
        new_locator = (PageOne.station[0], update_xpath)

        field = self.__browser.find_element(*PageOne.metro)
        field.click()

        station = self.__browser.find_element(*new_locator)
        self.__browser.execute_script(
            "arguments[0].scrollIntoView();", station)
        station.click()

    @allure.step("Заполняем поле Телефон")
    def write_telephon(self, phone):
        field = self.__browser.find_element(*PageOne.phone)
        field.send_keys(phone)

    @allure.step("Нажимаем кнопку Далее")
    def enter_button_form(self):
        button = self.__browser.find_element(*PageOne.button)
        button.click()

    @allure.step("Заполняем форму бронирования самоката, превая страница")
    def complete_form(self, fname, lname, address, metro, phone):
        self.write_first_name(fname)
        self.write_last_name(lname)
        self.write_address(address)
        self.choise_metro_stantion(metro)
        self.write_telephon(phone)
        self.enter_button_form()

    @allure.step("Очищаем поле Имя")
    def clean_first_name(self):
        field = self.__browser.find_element(*PageOne.first_name)
        ClearField()(field)

    @allure.step("Очищаем поле Фамилия")
    def clean_last_name(self):
        field = self.__browser.find_element(*PageOne.last_name)
        ClearField()(field)

    @allure.step("Очищаем поле Адрес")
    def clean_address(self):
        field = self.__browser.find_element(*PageOne.address)
        ClearField()(field)

    @allure.step("Очищаем поле Телефон")
    def clean_telephon_nubmer(self):
        field = self.__browser.find_element(*PageOne.phone)
        ClearField()(field)

    @allure.step("Очищаем форму бронирования самоката, превая страница")
    def clean_form(self):
        self.clean_first_name()
        self.clean_last_name()
        self.clean_address()
        self.clean_telephon_nubmer()


class OrderPageTwo:
    def __init__(self, browser):
        self.__browser = browser

    @allure.step("Выбираем дату")
    def choise_date(self, date):
        field = self.__browser.find_element(*PageTwo.date)
        field.send_keys(date)
        field.send_keys(Keys.ENTER)

    @allure.step("Выбараем срок аренды")
    def choise_rent(self, rend_day):
        field = self.__browser.find_element(*PageTwo.rent)
        field.click()
        update_locator = PageTwo.day[1].format(rend_day.strip())
        new_locator = (PageTwo.day[0], update_locator)
        day = self.__browser.find_element(*new_locator)
        self.__browser.execute_script("arguments[0].scrollIntoView();", day)
        day.click()

    @allure.step("Выбираем цвет")
    def choise_color(self, color):
        update_locator = PageTwo.checkbox[1].format(color.strip())
        new_locator = (PageTwo.checkbox[0], update_locator)
        field = self.__browser.find_element(*new_locator)
        field.click()

    @allure.step("Заполняем поле Комментарий")
    def write_comment(self, comment):
        field = self.__browser.find_element(*PageTwo.comment)
        field.send_keys(comment)

    @allure.step("Нажимаем на кнопку Далее")
    def enter_button_form(self):
        button = self.__browser.find_element(*PageTwo.order)
        button.click()

    @allure.step("Нажимаем на кнопку Назад")
    def back_button_form(self):
        button = self.__browser.find_element(*PageTwo.back)
        button.click()

    @allure.step("Нажимаем на кнопку подтвердить")
    def confirm(self):
        button = self.__browser.find_element(*PageConfirm.yes)
        button.click()

    @allure.step("Получаем результат бронирования самоката")
    def return_status_order(self):
        text = self.__browser.find_element(*PageConfirm.order).text
        return text

    @allure.step("Заполняем форму бронирования самоката, вторая страница")
    def complete_form(self, date, rend_day, color, comment):
        self.choise_date(date)
        self.choise_rent(rend_day)
        self.choise_color(color)
        self.write_comment(comment)
        self.enter_button_form()
        self.confirm()
