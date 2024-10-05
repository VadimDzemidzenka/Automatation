import pytest
import requests

URL = "https://x-clients-be.onrender.com"

@pytest.fixture()
def get_token(username='raphael', password='cool-but-crude'):
    log_pss = {"username": username, "password": password}
    resp_token = requests.post(URL + '/auth/login', json=log_pss)
    token = resp_token.json()["userToken"]
    return token