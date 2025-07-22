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
    """Инициализация Edge"""
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
    submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()

    # Ждём исчезновения кнопки submit (чтобы стили обновились)
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                            'button[type="submit"]'))
    )

    # Список зелёных полей
    green_fields = [        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    # Проверяем, что все зелёные поля действительно зелёные
    for field_id in green_fields:
        elem = driver.find_element(By.ID, field_id)
        border = elem.value_of_css_property("border-color")
        assert border == "rgb(40, 167, 69)", (
            f"Поле {field_id} должно быть зелёным, а цвет: {border}"
        )

    # Отдельно проверяем, что zip-code — красный
    zip_el = driver.find_element(By.ID, "zip-code")
    zip_border = zip_el.value_of_css_property("border-color")
    assert zip_border == "rgb(220, 53, 69)", \
        f"Поле zip-code должно быть красным, а цвет: {zip_border}"
