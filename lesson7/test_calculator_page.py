"""Калькулятор"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson7.calculator_page import CalculatorPage

@pytest.fixture
def browser():
    """Инициализация Chrome."""
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    """Проверяет работу калькулятора с задержкой через Page Object."""
    page = CalculatorPage(browser)
    page.open()
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    page.wait_for_result("15")
    # ассерт не нужен: если результат не появился, тест сам упадёт на wait
