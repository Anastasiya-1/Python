"""Главная страница"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    """Главная страница магазина (список товаров)."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    def add_products(self, *item_ids):
        """Добавляет товары в корзину по их item_id."""
        for item_id in item_ids:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, item_id)))
            btn.click()
    def go_to_cart(self):
        """Переходит в корзину."""
        cart_link = self.wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()
