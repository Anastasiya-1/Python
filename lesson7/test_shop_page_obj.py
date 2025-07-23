"""Проверка суммы заказа на saucedemo.com с использованием Page Object."""

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from lesson7.page_login import LoginPage
from lesson7.page_products import ProductsPage
from lesson7.page_cart import CartPage
from lesson7.page_checkout import CheckoutPage

@pytest.fixture
def browser():
    """Возвращает экземпляр Firefox."""
    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

def test_shop_total(browser):
    """Покупка 3 товаров, проверка итоговой суммы."""
    login = LoginPage(browser)
    products = ProductsPage(browser)
    cart = CartPage(browser)
    checkout = CheckoutPage(browser)

    login.open()
    login.login("standard_user", "secret_sauce")
    products.add_products(
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    )
    products.go_to_cart()
    cart.checkout()
    checkout.fill_form("Анастасия", "Ландарь", "625039")
    total = checkout.get_total()
    assert total == "Total: $58.29", f"Ожидалось 'Total: $58.29', получено '{total}'"
