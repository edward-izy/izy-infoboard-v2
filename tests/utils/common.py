# Commonly used test case functions.
import json

from tests.utils.data_dicts import DataDicts


# ------ Login / User Endpoints ------
def register_user(self, data):
    return self.client.post(
        "/auth/register", data=json.dumps(data), content_type="application/json",
    )


def login_user(self, email, password):
    return self.client.post(
        "/auth/login",
        data=json.dumps(dict(email=email, password=password,)),
        content_type="application/json",
    )


def get_token(self):
    register_user(self, DataDicts.user)
    login_res = login_user(self, email=DataDicts.user["email"], password=DataDicts.user["password"])
    login_data = json.loads(login_res.data.decode())
    token = "Bearer " + login_data["access_token"]
    return token


# ------ News Endpoints ------
def get_all_news(self, token):
    return self.client.get("/api/news/",
                           content_type="application/json",
                           headers={"Authorization": token})


def post_news(self, data, token):
    return self.client.post("/api/news/",
                            data=json.dumps(data),
                            content_type="application/json",
                            headers={"Authorization": token})


def update_news(self, data, token):
    return self.client.put("/api/news/",
                           data=json.loads(data),
                           content_type="application/json",
                           headers={"Authorization": token})


# ------ SFA Endpoints ------
def get_all_sfa(self, token):
    return self.client.get("/api/sprintfocusarea/",
                           content_type="application/json",
                           headers={"Authorization": token})


def post_sfa(self, data, token):
    return self.client.post("/api/sprintfocusarea/",
                            data=json.dumps(data),
                            content_type="application/json",
                            headers={"Authorization": token})


def update_sfa(self, data, token):
    return self.client.put("/api/sprintfocusarea/",
                           data=json.dumps(data),
                           content_type="application/json",
                           headers={"Authorization": token})


def get_by_sprint_sfa(self, token):
    return self.client.get("/api/sprintfocusarea/by-sprint",
                            query_string={"sprint": "1.40"},
                            content_type="application/json",
                            headers={"Authorization": token})