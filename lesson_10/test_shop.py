import pytest
import allure
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

@allure.title("Проверка итоговой суммы заказа на saucedemo.com")
@allure.description("Тестирует добавление трёх товаров в корзину и проверяет, что итоговая сумма заказа — $58.29.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total(browser):
    """Покупка 3 товаров и проверка итоговой суммы."""
    login = LoginPage(browser)
    products = ProductsPage(browser)
    cart = CartPage(browser)
    checkout = CheckoutPage(browser)

    with allure.step("Открыть страницу авторизации и войти"):
        login.open()
        login.login("standard_user", "secret_sauce")
    with allure.step("Добавить 3 товара в корзину"):
        products.add_products(
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        )
    with allure.step("Перейти в корзину и начать оформление заказа"):
        products.go_to_cart()
        cart.checkout()
    with allure.step("Заполнить форму покупателя и перейти к итогам"):
        checkout.fill_form("Анастасия", "Ландарь", "625039")
    with allure.step("Получить и проверить итоговую сумму"):
        total = checkout.get_total()
        with allure.step("Проверка, что сумма заказа равна 'Total: $58.29'"):
            assert total == "Total: $58.29", f"Ожидалось 'Total: $58.29', получено '{total}'"
