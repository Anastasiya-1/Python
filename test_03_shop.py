"""Покупка товаров в saucedemo.com и проверка итоговой суммы."""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def browser():
    """Фикстура, возвращающая экземпляр Firefox."""
    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

def test_shop_total(browser):
    """Проходит покупку 3 товаров и проверяет итоговую стоимость."""
    wait = WebDriverWait(browser, 15)
    browser.get("https://www.saucedemo.com/")

    # Авторизация
    user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    user_input.send_keys("standard_user")
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_btn = browser.find_element(By.ID, "login-button")
    login_btn.click()

    # Добавление товаров в корзину
    items = [        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for item_id in items:
        btn = wait.until(EC.element_to_be_clickable((By.ID, item_id)))
        btn.click()

    # Переход в корзину
    cart_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_btn.click()

    # Checkout
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    # Заполняем форму
    first = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    first.send_keys("Анастасия")
    last = browser.find_element(By.ID, "last-name")
    last.send_keys("Ландарь")
    postal = browser.find_element(By.ID, "postal-code")
    postal.send_keys("625039")
    continue_btn = browser.find_element(By.ID, "continue")
    continue_btn.click()

    # Проверка итоговой суммы
    total_lbl = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_lbl.text.strip()  # например, 'Total: $58.29'

    assert total_text.endswith("$58.29"), f"Ожидалось '$58.29', получено '{total_text}'"
