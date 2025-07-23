"""Форма"""

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from lesson7.form_page import FormPage


@pytest.fixture
def driver():
    """Инициализация Edge WebDriver для теста формы."""
    service = EdgeService(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_form_field_colors_pageobject(driver):
    """Проверяет, что zip-code подсвечен красным, остальные поля — зелёным."""
    form = FormPage(driver)
    form.open()
    # Заполняем форму
    form.fill_field('first-name', 'Иван')
    form.fill_field('last-name', 'Петров')
    form.fill_field('address', 'Ленина, 55-3')
    form.fill_field('e-mail', 'test@skypro.com')
    form.fill_field('phone', '+7985899998787')
    # Zip-code ПРОПУСКАЕМ (оставляем пустым)
    form.fill_field('city', 'Москва')
    form.fill_field('country', 'Россия')
    form.fill_field('job-position', 'QA')
    form.fill_field('company', 'Skypro')

    form.submit_form()

    green_fields = [        'first-name', 'last-name', 'address', 'e-mail', 'phone',
        'city', 'country', 'job-position', 'company'
    ]
    for field_id in green_fields:
        border = form.get_border_color(field_id)
        assert border == 'rgb(40, 167, 69)', (
            f'Field {field_id} should be green, got: {border}'
        )

    border_zip = form.get_border_color('zip-code')
    assert border_zip == 'rgb(220, 53, 69)', (
        f'Zip code should be red, got: {border_zip}'
    )
