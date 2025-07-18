"""
Нажать на кнопку
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
try:
    driver.get("http://uitestingplayground.com/ajax")
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

    # Ждём появления зелёного сообщения
    wait = WebDriverWait(driver, 10)
    success = wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".bg-success"),
            "Data loaded with AJAX get request."
        )
    )
    message = driver.find_element(By.CSS_SELECTOR, ".bg-success").text
    print(message.strip())
finally:
    driver.quit()
