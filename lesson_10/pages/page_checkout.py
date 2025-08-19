from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    """
    Page Object страница оформления заказа (Checkout).
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация CheckoutPage.

        :param driver: WebDriver — драйвер браузера
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def fill_form(self, first: str, last: str, postal: str) -> None:
        """
        Заполняет форму (имя, фамилия, почтовый индекс) и жмёт "Continue".

        :param first: Имя покупателя
        :param last: Фамилия покупателя
        :param postal: Почтовый индекс
        :return: None
        """
        fname = self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        fname.send_keys(first)
        lname = self.wait.until(
            EC.visibility_of_element_located((By.ID, "last-name"))
        )
        lname.send_keys(last)
        pcode = self.wait.until(
            EC.visibility_of_element_located((By.ID, "postal-code"))
        )
        pcode.send_keys(postal)
        btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        btn.click()

    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа (например, 'Total: $58.29').

        :return: str — строка с итоговой суммой
        """
        label = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return label.text.strip()
