"""Калькулятор"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    """Инициализация Chrome."""
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    """Проверяет работу калькулятора с задержкой."""
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)

    delay_input = browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    wait = WebDriverWait(browser, 45)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

    screen = browser.find_element(By.CSS_SELECTOR, "div.screen")
    assert screen.text.strip() == "15", f"На экране калькулятора: {screen.text}"
