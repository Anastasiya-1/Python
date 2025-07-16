"""
Дождаться картинки
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 15)
    # Ждём, когда у третьей картинки появится src
    all_imgs = wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, "img"))
    wait.until(
        lambda d: (
            all_imgs[2].get_attribute("src")
            and not all_imgs[2].get_attribute("src").endswith("blank.png")
        )
    )
    src = all_imgs[2].get_attribute("src")
    print(src)
finally:
    driver.quit()
