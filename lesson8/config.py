import pytest
import requests
from lesson8.autoexec import x_clients_URL

@pytest.fixture()
def get_token(username='raphael', password='cool-but-crude'):
    log_pss = {"username": username, "password": password}
    resp_token = requests.post(x_clients_URL + '/auth/login', json=log_pss)
    token = resp_token.json()["userToken"]
    return token
