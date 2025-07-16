"""
Упражнение 2. Клик по кнопке без ID
"""

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()

sleep(2)
driver.quit()
