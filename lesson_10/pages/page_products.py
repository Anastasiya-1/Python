from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    """
    Главная страница магазина (список товаров).

    Атрибуты:
        driver: WebDriver — экземпляр браузерного драйвера
        wait: WebDriverWait — явное ожидание для элементов
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация ProductsPage.

        :param driver: WebDriver — драйвер браузера
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_products(self, *item_ids: str) -> None:
        """
        Добавляет товары в корзину по их id.

        :param item_ids: Перечень id кнопок для товаров (str)
        :return: None
        """
        for item_id in item_ids:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, item_id)))
            btn.click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину покупателя.

        :return: None
        """
        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()
