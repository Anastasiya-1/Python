"""Форма"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """нициализация Edge"""
    service = EdgeService(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_form_field_colors(driver):
    """цвет поля"""
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    # Заполняем поля
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.ID, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.ID, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.ID, "city").send_keys("Москва")
    driver.find_element(By.ID, "country").send_keys("Россия")
    driver.find_element(By.ID, "job-position").send_keys("QA")
    driver.find_element(By.ID, "company").send_keys("SkyPro")

    # Отправляем форму
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Ожидаем, что появятся отметки валидации у всех полей (до 5 сек)
    wait = WebDriverWait(driver, 5)
    fields = [        ("zip-code", False),  # должен быть с ошибкой (красный)
        ("first-name", True),
        ("last-name", True),
        ("address", True),
        ("e-mail", True),
        ("phone", True),
        ("city", True),
        ("country", True),
        ("job-position", True),
        ("company", True)
    ]

    # Проверим подсветку каждого поля формы
    for field_id, should_be_green in fields:
        input_elem = driver.find_element(By.ID, field_id)
        # Ждём появления бордера (либо красного, либо зелёного)
        wait.until(lambda d, elem=input_elem: (
             elem.value_of_css_property("border-color")
             in ("rgb(40, 167, 69)", "rgb(220, 53, 69)")
             ))

        border_color = input_elem.value_of_css_property("border-color")
        if should_be_green:
            # Зеленый: rgb(40, 167, 69)
            assert border_color == "rgb(40, 167, 69)", (
            f"Поле {field_id} должно быть зелёным, но {border_color}")
        else:
            # Красный: rgb(220, 53, 69)
            assert border_color == "rgb(220, 53, 69)", (
            f"Поле {field_id} должно быть красным, но {border_color}")
