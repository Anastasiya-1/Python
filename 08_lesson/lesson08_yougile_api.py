import requests

class YougileAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_project(self, name):  # [POST] /api-v2/projects
        return requests.post(
            f"{self.base_url}/api-v2/projects",
            json={"name": name},
            headers=self.headers
        )

    def update_project(self, project_id, name):  # [PUT] /api-v2/projects/{id}
        return requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            json={"name": name},
            headers=self.headers
        )

    def get_project(self, project_id):  # [GET] /api-v2/projects/{id}
        return requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )
