
import allure

from ..urls.urls import URLS
from ..pages.header_page import HeaderPage
from ..utilities.wait import Wait
from ..locators.dzen import DzenLocator


class TestRedirectHeader:
    "Тест кейс кнопок в header"

    @allure.title("""Тест: проверка перенаправление на dzen,
                после нажатия на логотип Yandex""")
    def test_click_logo_yandex_redirect_home_page_ya(self, browser_def):
        browser_def.get(URLS['home'])
        header = HeaderPage(browser_def)
        header.click_yandex_logo()
        new_window = browser_def.window_handles[1]
        browser_def.switch_to.window(new_window)
        Wait.element(browser_def, DzenLocator.search)
        current_url = browser_def.current_url
        assert "dzen.ru" in current_url

    @allure.title("""Тест: проверка перенаправления на главную страницу,
                после нажатия на логотип Самокат""")
    def test_click_logo_scooter_redirect_home_page_scooter(self, browser_def):
        browser_def.get(URLS['home'])
        header = HeaderPage(browser_def)
        header.click_order()
        header.click_scooter_logo()
        current_url = browser_def.current_url
        assert current_url in URLS['home']
