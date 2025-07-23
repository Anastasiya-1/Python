"""Авторизация"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Cтраница авторизации saucedemo.com."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    def open(self):
        """Открывает страницу авторизации."""
        self.driver.get("https://www.saucedemo.com/")
    def login(self, username, password):
        """Выполняет вход на saucedemo.com с указанными логином и паролем."""
        user_input = self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        user_input.send_keys(username)
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys(password)
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        btn.click()
