from lesson8.Pages.ToDo import Task
from lesson8.config import*
from lesson8.autoexec import*

zadacha = Task()

def test_todo():
        #Список задач
    list = zadacha.get_list()
        #status_code 200
    assert list.status_code == 200
    

    
        #Создание новой задачи 
    params = {"title": "Школа", "completed": 'false'}
    task = zadacha.create(params)
        #Проверяем ID
    assert task is not None
    
    
        #Переименование задачи 
    params = {"title": "Школа - 1 сентября"} 
    renamed_task = zadacha.rename (task, params)
        #Проверяем изменения 
    assert renamed_task.json()['title'] == "Школа - 1 сентября"
    
    
        #Получение информации по созданной задаче 
    info = zadacha.info(task)
        #Проверяем название 
    assert info.json()['title'] == "Школа - 1 сентября"
        #Проверяем ID 1 = ID 2 
    assert info.json()["id"] == task
    
     
        #Задача выполненна 
    params = {"completed": 'true'}
    satus_true = zadacha.change_status(task, params)
        #Проверяем что задача true
    assert satus_true == True
    
    
        #Снятие отметки (выполненна)
    params = {"completed": 'false'}
    satus_false = zadacha.change_status(task, params)
        #Проверяем что задача False
    assert satus_false == False
    
    
        #Удаление задачи 
    deleting = zadacha.delete(task)
        #status_code 200
    assert deleting == 200