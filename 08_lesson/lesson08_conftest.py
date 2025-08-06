import pytest
from yougile_api import YougileAPI

@pytest.fixture(scope="session")
def api():
    # Заменить на реальные значения перед запуском тестов!
    base_url = "https://api.yougile.com"
    token = "ВАШ_ТОКЕН"
    return YougileAPI(base_url, token)
