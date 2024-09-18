import pytest
from lesson9.Pages.Employee import Employer
from lesson9.Pages.DataBase import DataBase

api = Employer('https://x-clients-be.onrender.com')
db = DataBase(
    "postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

# Получаем список сотрудников из БД и АПИ, после чего сравниваем их 
def test_get_list_of_employers():
    # БД - Создаем компанию
    db.create_company('Made_Minsk', 'Made_Minks')
    # БД - Получаем ID последней созданной компании
    max_id = db.last_company_id()
    # БД - добавляем сотрудника в компанию
    db.create_employer(max_id, "Vadzim", "Dzemidzenka", 375292606021)
    # БД - Получаем список сотрудников из последней созданной компании 
    db_employer_list = db.get_list_employer(max_id)
    # API - Получаем список сотрудников из последней созданной компании 
    api_employer_list = api.get_list(max_id)
    # Сравниваем списки сотрудников полученных ид БД и через АРІ 
    assert len(db_employer_list) == len (api_employer_list)
    # Удаляем сотрудника компании, иначе компания не удалится 
    response = (api.get_list(max_id))[0]
    employer_id = response["id"] 
    db.delete_employer (employer_id)
    # БД - Удаляем последнюю созданную компанию
    db.delete(max_id)

# Добавляем сотрудника в БД и сравниваем с АПИ имя, статус и фамилию 
def test_add_new_employer():
    db.create_company('Made_Minsk adding new employer', 'employer') 
    max_id = db.last_company_id()
    db.create_employer(max_id, "Vadzim", "Dzemidzenka", 375292606021) 
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    # Сравниваем ID компании
    assert response["companyId"] == max_id 
    # Сравниваем имя сотрудника с заданным 
    assert response["firstName"] == "Vadzim"
    # Удостоверяемся что статус сотрудника True
    assert response["isActive"] == True
    # Сравниваем фамилию сотрудника с заданной
    assert response["lastName"] == "Dzemidzenka" 
    # БД - удаляем созданного сотрудника
    db.delete_employer(employer_id)
    # БД - Удаляем последнюю созданную компанию
    db.delete(max_id)

# Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании в БД 
def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Vadzim", "Dzemidzenka", 375292606021)
    employer_id = db.get_employer_id(max_id)
    # Сравниваем информацию о сотруднике полученную по API с информацией указанной при создании в БД  
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Vadzim"
    assert get_api_info["lastName"] == "Dzemidzenka"
    assert get_api_info["phone"] == "375292606021"
    # БД - удаляем созданного сотрудника
    db.delete_employer (employer_id)
    # БД - Удаляем последнюю созданную компанию
    db.delete(max_id)

# Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике
def test_update_user_info():
    db.create_company('New updating company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Vadzim", "Dzemidzenka", 375292606021)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("WARRIOR", employer_id)
    # Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "WARRIOR"
    assert get_api_info["lastName"] == "Dzemidzenka"
    assert get_api_info["isActive"] == True
    # БД - удаляем созданного сотрудника
    db.delete_employer(employer_id)
    # БД - Удаляем последнюю созданную компанию
    db.delete(max_id)