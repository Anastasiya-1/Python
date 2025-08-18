import pytest
import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@allure.title("Проверка сложения 7 + 8 на калькуляторе с задержкой")
@allure.description("Тест выполняет 7 + 8 на slow-calculator с задержкой 45с")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_sum():
    """Проверяет правильное сложение с задержкой."""
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)
        with allure.step("Открыть страницу калькулятора"):
            page.open()
        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(45)
        with allure.step("Ввести выражение 7 + 8"):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
        with allure.step("Выполнить вычисление (нажать =)"):
            page.click_button("=")
        with allure.step("Дождаться и проверить результат '15'"):
            page.wait_for_result("15")
            actual = driver.find_element_by_css_selector("div.screen").text.strip()
            with allure.step("Проверяем, что результат равен 15"):
                assert actual == "15", f"Ожидалось 15, получено '{actual}'"
    finally:
        driver.quit()
