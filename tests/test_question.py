import allure
from ..urls.urls import URLS
from ..utilities.utilits import scrol_for_element
from ..utilities.wait import Wait

from ..pages.home_page import Question


class TestQuestion:

    @allure.title("Тест проверка появление ответа вопрос-ответ 1")
    def test_question_n_0(self, browser_def):
        "тест: проверка раскрытия ответа на вопрос под номером 0"
        browser_def.get(URLS['home'])
        number_question = 0
        quest = Question(browser_def)
        answer = quest.get_answer(number_question)
        status = quest.answer_status_hidden(answer)
        assert status
        question = quest.get_question(0)
        scrol_for_element(browser_def, question)
        Wait.click(browser_def, element=question)
        status = quest.answer_status_hidden(answer)
        assert status is None

    @allure.title("Тест проверка появление ответа вопрос-ответ 2")
    def test_question_n_1(self, browser_def):
        "тест: проверка раскрытия ответа на вопрос под номером 1"
        browser_def.get(URLS['home'])
        number_question = 1
        quest = Question(browser_def)
        answer = quest.get_answer(number_question)
        status = quest.answer_status_hidden(answer)
        assert status
        question = quest.get_question(number_question)
        scrol_for_element(browser_def, question)
        Wait.click(browser_def, element=question)
        status = quest.answer_status_hidden(answer)
        assert status is None

    @allure.title("Тест проверка появление ответа вопрос-ответ 3")
    def test_question_n_2(self, browser_def):
        "тест: проверка раскрытия ответа на вопрос под номером 2"
        browser_def.get(URLS['home'])
        number_question = 2
        quest = Question(browser_def)
        answer = quest.get_answer(number_question)
        status = quest.answer_status_hidden(answer)
        assert status
        question = quest.get_question(number_question)
        scrol_for_element(browser_def, question)
        Wait.click(browser_def, element=question)
        status = quest.answer_status_hidden(answer)
        assert status is None

    @allure.title("Тест проверка появление ответа вопрос-ответ 4")
    def test_question_n_3(self, browser_def):
        "тест: проверка раскрытия ответа на вопрос под номером 3"
        browser_def.get(URLS['home'])
        number_question = 3
        quest = Question(browser_def)
        answer = quest.get_answer(number_question)
        status = quest.answer_status_hidden(answer)
        assert status
        question = quest.get_question(number_question)
        scrol_for_element(browser_def, question)
        Wait.click(browser_def, element=question)
        status = quest.answer_status_hidden(answer)
        assert status is None

    @allure.title("Тест проверка появление ответа вопрос-ответ 5")
    def test_question_n_4(self, browser_def):
        "тест: проверка раскрытия ответа на вопрос под номером 4"
        browser_def.get(URLS['home'])
        number_question = 4
        quest = Question(browser_def)
        answer = quest.get_answer(number_question)
        status = quest.answer_status_hidden(answer)
        assert status
        question = quest.get_question(number_question)
        scrol_for_element(browser_def, question)
        Wait.click(browser_def, element=question)
        status = quest.answer_status_hidden(answer)
        assert status is None

    @allure.title("Тест проверка появление ответа вопрос-ответ 6")
    def test_question_n_5(self, browser_def):
        "тест: проверка раскрытия ответа на вопрос под номером 5"
        browser_def.get(URLS['home'])
        number_question = 5
        quest = Question(browser_def)
        answer = quest.get_answer(number_question)
        status = quest.answer_status_hidden(answer)
        assert status
        question = quest.get_question(number_question)
        scrol_for_element(browser_def, question)
        Wait.click(browser_def, element=question)
        status = quest.answer_status_hidden(answer)
        assert status is None

    @allure.title("Тест проверка появление ответа вопрос-ответ 7")
    def test_question_n_6(self, browser_def):
        "тест: проверка раскрытия ответа на вопрос под номером 6"
        browser_def.get(URLS['home'])
        number_question = 6
        quest = Question(browser_def)
        answer = quest.get_answer(number_question)
        status = quest.answer_status_hidden(answer)
        assert status
        question = quest.get_question(number_question)
        scrol_for_element(browser_def, question)
        Wait.click(browser_def, element=question)
        status = quest.answer_status_hidden(answer)
        assert status is None
