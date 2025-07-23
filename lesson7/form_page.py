"""Форма"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """Page Object для работы с формой на bonigarcia.dev."""

    def __init__(self, driver):
        """Инициализация страницы формы."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открывает страницу с формой."""
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
        )

    def fill_field(self, field_id, value):
        """Заполняет указанное поле формы значением."""
        elem = self.wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        elem.clear()
        elem.send_keys(value)

    def submit_form(self):
        """Отправляет форму и ожидает завершения валидации."""
        submit = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        submit.click()
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, 'button[type="submit"]')
            )
        )

    def get_border_color(self, field_id):
        """Возвращает цвет рамки указанного поля."""
        elem = self.wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        return elem.value_of_css_property('border-color')
