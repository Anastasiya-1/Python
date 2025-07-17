"""Дождаться загрузки всех картинок и вывести src третей."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait = WebDriverWait(driver, 15)

    # 1. Явно ждём, что на странице есть минимум 3 картинки
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "img")) >= 3)

    def third_img_loaded(d):
        """
        Проверяет, загружено ли третье изображение на странице
        """
        imgs = d.find_elements(By.CSS_SELECTOR, "img")
        if len(imgs) < 3:
            return False
        src = imgs[2].get_attribute("src")
        if src and not src.endswith("blank.png"):
            return src
        return False

    # 2. Ждём, что третья картинка загружена (src действительный)
    src = wait.until(third_img_loaded)
    print(src)
finally:
    driver.quit()
