"""
Переименовать кнопку
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
try:
    driver.get("http://uitestingplayground.com/textinput")
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")
    driver.find_element(By.ID, "updatingButton").click()

    # Ждём изменения текста на кнопке
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "updatingButton"),
            "SkyPro"
        )
    )

    button_text = driver.find_element(By.ID, "updatingButton").text
    print(button_text.strip())
finally:
    driver.quit()
