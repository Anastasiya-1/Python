import requests

BASE_URL = "https://api.yougile.com"

class YougileAPI:
    def __init__(self, token):
        self.base_url = BASE_URL
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_project(self, title):  # [POST] /api-v2/projects
        return requests.post(
            f"{self.base_url}/api-v2/projects",
            json={"title": title},
            headers=self.headers
        )

    def update_project(self, project_id, title):  # [PUT] /api-v2/projects/{id}
        return requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            json={"title": title},
            headers=self.headers
        )

    def get_project(self, project_id):  # [GET] /api-v2/projects/{id}
        return requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )
