"""Корзина товаров"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    """Корзина товаров."""

    def __init__(self, driver):
        """Инициализация страницы корзины."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def checkout(self):
        """Нажимает кнопку оформления заказа (Checkout)."""
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        btn.click()
