 # Как запустить тесты для формирования отчета :

 1.Подключите Allure: pip install allure-pytest
 2.Запустите тесты и укажите путь к каталогу результатов тестирования: python -m pytest --alluredir allure-result
 3.В директории с тестами появится папка allure-result. Там сохранятся отчеты о тестах

 # Как просмотреть сформированный отчет :
 1.Команда ниже запускает Allure и конвертирует результаты теста в отчет: allure serve allure-result
 2.Чтобы терминал распознал команду allure , установите Allure Report. 
   Пользователи Windows: запустите в терминале VS Code команду : 
    1. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    2. Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
 3.Затем команду scoop install allure 
 4.Введите команду ниже — сгенерируется отчет о тестах: allure serve allure-results

 Отчет откроется на локальном сервере в окне вашего браузера.
Overview — раздел с общей информацией: сколько всего тестов запустили, процент успешных тестов, доля успешных и неуспешных тестов.
Suits — список тестов и конкретная информация о каждом из них.