import pytest
import allure
from lesson10.HW9.Pages.Employee import Employer
from lesson10.HW9.Pages.DataBase import DataBase

api = Employer('https://x-clients-be.onrender.com')
db = DataBase(
    "postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")



@allure.epic("X-clients")
@allure.severity (severity_level='normal') 
@allure.title("Список сотрудников")
@allure.description("Получаем список сотрудников из БД и АПИ, после чего сравниваем их") 
@allure.feature('Тест 1')
def test_get_list_of_employers():
    with allure.step("БД - Создаем компанию"):
        db.create_company('Made_Minsk', 'Made_Minks')
    with allure.step("БД - Получаем ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("БД - добавляем сотрудника в компанию"):
        db.create_employer(max_id, "Vadzim", "Dzemidzenka", 375292606021)
    with allure.step("БД - Получаем список сотрудников из последней созданной компании"):
        db_employer_list = db.get_list_employer(max_id)
    with allure.step("API - Получаем список сотрудников из последней созданной компании"):
        api_employer_list = api.get_list(max_id)
    with allure.step("Сравниваем списки сотрудников полученных ид БД и через АРІ"):
        assert len(db_employer_list) == len (api_employer_list)
    with allure.step("Удаляем сотрудника компании, иначе компания не удалится"):
        response = (api.get_list(max_id))[0]
        employer_id = response["id"] 
        db.delete_employer (employer_id)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity (severity_level='crirical') 
@allure.title("Добовление сотрудников")
@allure.description("Добавляем сотрудника в БД и сравниваем с АПИ имя, статус и фамилию") 
@allure.feature('Тест 2')
def test_add_new_employer():
    with allure.step("БД - Получаем ID компании"):
        db.create_company('Made_Minsk adding new employer', 'employer') 
        max_id = db.last_company_id()
    with allure.step("БД - Получаем ID сотрудника"):
        db.create_employer(max_id, "Vadzim", "Dzemidzenka", 375292606021) 
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
    with allure.step("Сравниваем ID компании"):
        assert response["companyId"] == max_id 
    with allure.step("Сравниваем имя сотрудника с заданным"):
        assert response["firstName"] == "Vadzim"
    with allure.step("Удостоверяемся что статус сотрудника True"):
        assert response["isActive"] == True
    with allure.step("Сравниваем фамилию сотрудника с заданной"):
        assert response["lastName"] == "Dzemidzenka" 
    with allure.step("удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("Удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity (severity_level='normal') 
@allure.title("Получение информации о сотруднике по ID")
@allure.description("Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании в БД") 
@allure.feature('Тест 3')
def test_assertion_data():
    with allure.step("БД - Получаем ID компании"):
        db.create_company('Employer get id company', 'new')
        max_id = db.last_company_id()
    with allure.step("БД - Получаем ID сотрудника"):
        db.create_employer(max_id, "Vadzim", "Dzemidzenka", 375292606021)
        employer_id = db.get_employer_id(max_id)
    with allure.step("Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании в БД"): 
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "Vadzim"
        assert get_api_info["lastName"] == "Dzemidzenka"
        assert get_api_info["phone"] == "375292606021"
    with allure.step("БД - удаляем созданного сотрудника"):
        db.delete_employer (employer_id)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity (severity_level='crirical') 
@allure.title("Обновление информации о сотруднике")
@allure.description("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике") 
@allure.feature('Тест 4')
def test_update_user_info():
    with allure.step("БД - Получаем ID компании"):
        db.create_company('New updating company', 'test')
        max_id = db.last_company_id()
    with allure.step("БД - Получаем ID сотрудника"):
        db.create_employer(max_id, "Vadzim", "Dzemidzenka", 375292606021)
        employer_id = db.get_employer_id(max_id)
    with allure.step("БД - Изменяем имя сотрудника"): 
        db.update_employer_info("WARRIOR", employer_id)
    with allure.step("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике"):
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "WARRIOR"
        assert get_api_info["lastName"] == "Dzemidzenka"
        assert get_api_info["isActive"] == True
    with allure.step("БД - удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete(max_id)