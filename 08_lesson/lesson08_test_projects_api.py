import pytest

@pytest.mark.usefixtures("api")
class TestProjectsAPI:
    def test_create_project_positive(self, api):
        resp = api.create_project("AutoTestProject")
        assert resp.status_code == 200
        data = resp.json()
        assert "id" in data
        assert data["name"] == "AutoTestProject"

    def test_create_project_negative(self, api):
        # Попытка создать проект без имени (или с пустым именем)
        resp = api.create_project("")
        assert resp.status_code in (400, 422)

    def test_update_project_positive(self, api):
        project = api.create_project("ProjForUpdate").json()
        project_id = project["id"]

        resp = api.update_project(project_id, "ProjUpdated")
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == project_id
        assert data["name"] == "ProjUpdated"

    def test_update_project_negative(self, api):
        # Обновление проекта с несуществующим id
        resp = api.update_project("nonexistent_id", "NewName")
        assert resp.status_code in (400, 404)

    def test_get_project_positive(self, api):
        project = api.create_project("ProjForGet").json()
        project_id = project["id"]

        resp = api.get_project(project_id)
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == project_id
        assert data["name"] == "ProjForGet"

    def test_get_project_negative(self, api):
        # Запрос проекта по несуществующему id
        resp = api.get_project("nonexistent_id")
        assert resp.status_code == 404
