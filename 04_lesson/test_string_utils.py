"""
Покрытие тестами методов класса StringUtils.
"""

import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    """
    Фикстура для создания экземпляра StringUtils для тестирования.
    """
    return StringUtils()


# ----------- capitalize -----------

def test_capitalize_regular(utils):
    """Позитивный тест: обычная строка преобразуется с заглавной буквы."""
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_first_upper(utils):
    """Позитивный тест: строка уже с заглавной буквы не меняется."""
    assert utils.capitalize("Skypro") == "Skypro"

def test_capitalize_empty_string(utils):
    """Негативный тест: пустая строка возвращает пустую строку."""
    assert utils.capitalize("") == ""

def test_capitalize_space_string(utils):
    """Негативный тест: строка с пробелом в начале не изменится."""
    assert utils.capitalize(" skypro") == " skypro"

def test_capitalize_numbers(utils):
    """Позитивный тест: строка с числами не изменяется."""
    assert utils.capitalize("123") == "123"

def test_capitalize_none(utils):
    """Негативный тест: попытка передать None вызывает AttributeError."""
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# ----------- trim -----------

def test_trim_left_spaces(utils):
    """Позитивный тест: удаляются пробелы только слева."""
    assert utils.trim("   skypro") == "skypro"

def test_trim_no_spaces(utils):
    """Позитивный тест: строка без пробелов не меняется."""
    assert utils.trim("skypro") == "skypro"

def test_trim_only_spaces(utils):
    """Негативный тест: строка только из пробелов становится пустой."""
    assert utils.trim("   ") == ""

def test_trim_empty_string(utils):
    """Негативный тест: пустая строка возвращает пустую строку."""
    assert utils.trim("") == ""

def test_trim_none(utils):
    """Негативный тест: попытка передать None вызывает AttributeError."""
    with pytest.raises(AttributeError):
        utils.trim(None)

def test_trim_right_spaces(utils):
    """Негативный тест: пробелы справа не удаляются."""
    assert utils.trim("skypro   ") == "skypro   "


# ----------- contains -----------

def test_contains_symbol_present(utils):
    """Позитивный тест: символ найден в строке."""
    assert utils.contains("SkyPro", "S") is True

def test_contains_symbol_absent(utils):
    """Позитивный тест: символ не найден в строке."""
    assert utils.contains("SkyPro", "U") is False

def test_contains_empty_string(utils):
    """Негативный тест: в пустой строке не может быть символа."""
    assert utils.contains("", "a") is False

def test_contains_empty_symbol(utils):
    """Граничный тест: пустой символ всегда есть в непустой строке."""
    assert utils.contains("SkyPro", "") is True

def test_contains_none(utils):
    """Негативный тест: попытка передать None вызывает AttributeError."""
    with pytest.raises(AttributeError):
        utils.contains(None, "S")
