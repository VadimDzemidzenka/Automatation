import requests
import json
import allure
from lesson10.HW9.conftest import URL

path = '/employee/'


class Company:
    """Класс компании Company"""
    def __init__(self, url=URL) -> str:
        self.url = url
        
    @allure.step("Создание компании")
    def create(self, token: str, body: json) -> str:
        headers = {"x-client-token": token}
        response = requests.post(
            self.url + "/company", headers=headers, params=body)
        return response.json()
    
    @allure.step("Последняя созданная активная компания")
    def last_active_company_id(self) -> int:
        active_params = {'active': 'true'}
        response = requests.get(
            self.url + "/company", params=active_params)
        return response.json()[-1]['id']
    

class Employer:
    """Класс сотрудников Employer"""
    def __init__(self, url=URL) -> str:
        self.url = url
    
    @allure.step("Список сотрудников компании")
    def get_list(self, company_id: int) -> int:
        company = {'company': company_id}
        response = requests.get(
            self.url + '/employee', params=company)
        return response.json()
    
    @allure.step("Добавление сотрудника в компанию")
    def add_new(self, token: str, body: json) -> str:
        headers = {"x-client-token": token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        return response.json()
    
    @allure.step("Получение информации о сотруднике")
    def get_info(self, employee_id: int) -> int:
        response = requests.get(self.url + path + str(employee_id))
        return response
    
    @allure.step("Изменение информации о сотруднике")
    def change_info(self, token: str, employee_id: int, body: json) -> int:
        headers = {'x-client-tocen': token}
        response = requests.patch(self.url + path + str(employee_id), headers=headers, json=body)
        return response