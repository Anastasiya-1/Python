"""Страница оформления заказа."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    """Страница оформления заказа."""

    def __init__(self, driver):
        """Инициализация CheckoutPage."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def fill_form(self, first, last, postal):
        """Заполняет форму: имя, фамилия, почтовый индекс и нажимает 'Continue'."""
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

    def get_total(self):
        """Возвращает строку с итоговой суммой (например, 'Total: $58.29')."""
        label = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return label.text.strip()
