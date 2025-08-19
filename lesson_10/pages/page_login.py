from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object: страница авторизации saucedemo.com
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        :param driver: WebDriver — объект браузера
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self) -> None:
        """
        Открывает страницу авторизации saucedemo.com.

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход с заданными логином и паролем.

        :param username: Логин (str)
        :param password: Пароль (str)
        :return: None
        """
        user_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        user_input.send_keys(username)
        password_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_input.send_keys(password)
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        btn.click()
