"""Калькулятор"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """Page Object для калькулятора."""

    def __init__(self, driver):
        """Инициализация страницы калькулятора."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, delay: int):
        """Устанавливает задержку в поле #delay."""
        field = self.wait.until(EC.visibility_of_element_located((By.ID, "delay")))
        field.clear()
        field.send_keys(str(delay))

    def click_button(self, value: str):
        """Нажимает кнопку на калькуляторе с текстом value."""
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{value}']"))
        )
        btn.click()

    def wait_for_result(self, result: str):
        """Ожидает на экране результат result."""
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), result)
        )
