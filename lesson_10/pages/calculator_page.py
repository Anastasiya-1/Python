"""Калькулятор PageObject."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """
    Page Object для калькулятора slow-calculator.
    Атрибуты:
        driver: WebDriver – экземпляр драйвера браузера
        wait: WebDriverWait – явное ожидание
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.
        :param driver: WebDriver – вебдрайвер Selenium
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60) # <= Запас времени!

    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        :return: None
        """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay: int) -> None:
        """
        Устанавливает задержку в поле #delay.
        :param delay: int — значение задержки в секундах
        :return: None
        """
        field = self.wait.until(EC.visibility_of_element_located((By.ID, "delay")))
        field.clear()
        field.send_keys(str(delay))

    def click_button(self, value: str) -> None:
        """
        Нажимает кнопку на калькуляторе с текстом.
        :param value: str — кнопка (цифра или операция)
        :return: None
        """
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{value}']")))
        btn.click()

    def wait_for_result(self, expected: str, timeout: int = 60) -> None:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.
        :param expected: ожидаемое значение (например, "15")
        :param timeout: максимальное время ожидания, секунд
        :return: строка с результатом
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "div.screen").text.strip() == expected)
        return self.driver.find_element(By.CSS_SELECTOR, "div.screen").text.strip()
