from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    """
    Page Object модель для страницы корзины товаров.

    Атрибуты:
        driver: WebDriver — экземпляр драйвера браузера.
        wait: WebDriverWait — явное ожидание для операций с элементами.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр Selenium WebDriver.
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def checkout(self) -> None:
        """
        Нажимает кнопку "Checkout" (оформить заказ).

        :return: None
        """
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        btn.click()
