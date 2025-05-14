import allure

from ..urls.urls import URLS
from ..pages.order_page import OrderPageOne, OrderPageTwo
from ..utilities.utilits import scrol_for_element
from ..utilities.wait import Wait
from ..locators.order import PageConfirm
from ..locators.header import HeaderLocator
from ..locators.home import HomeLocator
from ..data.form import DataOrderForm


class TestOrderCase:
    "Тест кейс бронирования самоката"

    @allure.title("""Тест: бронирование самоката,
                нажатием на кнопку в шапке странице""")
    def test_order_rus_first_last_name_button_header(self, browser_def):
        """тест: бронирование самоката, нажатием на кнопку в шапке странице"""
        browser_def.get(URLS['home'])
        browser_def.find_element(*HeaderLocator.order).click()
        data = DataOrderForm.get_data()
        order = OrderPageOne(browser_def)
        order.complete_form(**data['page_one'])
        order = OrderPageTwo(browser_def)
        order.complete_form(**data['page_two'])
        status = order.return_status_order()
        assert PageConfirm.text in status

    @allure.title("""Тест: бронирование самоката,
                нажатием на кнопку на главной странице,с новыми данными""")
    def test_order_end_first_last_name_button_home_page(self, browser_def):
        """
        тест: бронирование самоката, нажатием на кнопку на главной странице,
        с новыми данными
        """
        browser_def.get(URLS['home'])
        button = browser_def.find_element(*HomeLocator.order)
        scrol_for_element(browser_def, button)
        Wait.click(browser_def, element=button)
        data = DataOrderForm.get_new_data()
        order = OrderPageOne(browser_def)
        order.complete_form(**data['page_one'])
        order = OrderPageTwo(browser_def)
        order.complete_form(**data['page_two'])
        status = order.return_status_order()
        assert PageConfirm.text in status
