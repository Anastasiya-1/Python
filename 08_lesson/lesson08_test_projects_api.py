import pytest
from lesson08_yougile_api import YougileAPI

class TestProjectsAPI:

    def test_create_project_positive(self):
        api = YougileAPI()
        resp = api.create_project("AutoTestProject")
        assert resp.status_code == 201
        data = resp.json()
        project_id = data.get("id")
        assert project_id is not None, "Не был получен ключ id ответе запроса создания проекта"

    def test_create_project_negative(self):
        api = YougileAPI()
        # Попытка создать проект без имени (или с пустым именем)
        resp = api.create_project("")
        assert resp.status_code == 400

    def test_update_project_positive(self):
        api = YougileAPI()
        project = api.create_project("ProjForUpdate").json()
        project_id = project.get("id")
        assert project_id is not None, "Не был получен ключ id ответе запроса создания проекта"

        resp = api.update_project(project_id, "ProjUpdated")
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("id") == project_id

    def test_update_project_negative(self):
        api = YougileAPI()
        # Обновление проекта с несуществующим id
        resp = api.update_project("nonexistent_id", "NewName")
        assert resp.status_code == 404

    def test_get_project_positive(self):
        api = YougileAPI()
        project = api.create_project("ProjForGet").json()
        project_id = project.get("id")
        assert project_id is not None, "Не был получен ключ id ответе запроса создания проекта"

        resp = api.get_project(project_id)
        assert resp.status_code == 200
        data = resp.json()
        assert data.get("id") == project_id
        assert data.get("title") == "ProjForGet"

    def test_get_project_negative(self):
        api = YougileAPI()
        # Запрос проекта по несуществующему id
        resp = api.get_project("nonexistent_id")
        assert resp.status_code == 404
