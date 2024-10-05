import pytest
from string_utils import StringUtils

utils = StringUtils()

#---------------capitilize-----------------------
def test_capitilize():
    #Позитивные проверки
    assert utils.capitilize("Vadzim") == "Vadzim"
    assert utils.capitilize("Vadzim dzemidzenka") == "Vadzim dzemidzenka"
    assert utils.capitilize("123456789") == "123456789"
    #Негативные проверки
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("1t2e3s4t") == "1t2e3s4t"


#-----------------trim---------------------------
def test_trim():
    #Позитивные проверки
    assert utils.trim("     privet") == "privet"
    assert utils.trim(" allo   ") == "allo   "
    assert utils.trim(" PPP   ") == "PPP   "
    #Негативные проверки
    assert utils.trim("") == ""

#----------------to_list------------------------
@pytest.mark.parametrize('string, delimeter, result', [
    #Позитивные проверки
    ("BMW,OPEL,AUDI", ",", ["BMW", "OPEL", "AUDI"]),
    ("0,9,8,6,5", ",", ["0", "9", "8", "6", "5"]),
    ("*@$@%@$", "@", ["*", "$", "%", "$"]),
    #Негативные проверки
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
])

def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result
    
#-----------------contains-----------------------
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки
    ("дорога", "д", True),
    ("минск", "к", True),
    ("сахар", "р", True),
    ("Минск-Пасажирский", "-", True),
    ("Немига3", "3", True),
    ("12345677890", "0", True),
    #Негативные проверки
    ("Гомель", "ж", False),
    ("1234567789", "0", False),
    ("карась", "К", False),
    ("hello", "р", False),  
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result
    
#-----------------delete_symbol-------------------
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки
    ("дорога", "д", "орога"),
    ("Молния", "я", "Молни"),
    ("Минск-Пасажирский", "П", "Минск-асажирский"),
    ("12345677890", "8", "1234567790"),
    ("Привет привет", " ", "Приветпривет"),
    #Негативные проверки
    ("дорога", "к", "дорога"),
    ("Молния", "1", "Молния"),
    ("Минск-Пасажирский", " ", "Минск-Пасажирский"),
    ("1234", "5", "1234"),
    ("Привет привет", "-", "Привет привет"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result
    
#-----------------starts_with-------------------
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки
    ("дорога", "д", True),
    ("минск", "м", True),
    ("сахар", "с", True),
    ("Минск-Пасажирский", "М", True),
    ("Немига3", "Н", True),
    ("12345677890", "1", True),
    #Негативные проверки
    ("Гомель", "г", False),
    ("1234567789", "0", False),
    ("карась", "К", False),
    ("hello", "H", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

#------------------end_with-------------------
@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные проверки
    ("дорога", "а", True),
    ("минск", "к", True),
    ("сахаР", "Р", True),
    ("Минск-Пасажирский", "й", True),
    ("Немига3", "3", True),
    ("12345677890", "0", True),
    #Негативные проверки
    ("Гомель", "г", False),
    ("1234567789", "0", False),
    ("карась", "К", False),
    ("hello", "H", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result
    
#------------------is_empty-------------------
@pytest.mark.parametrize('string, result', [
    #Позитивные проверки
    ("", True),
    (" ", True),
    ("  ", True),
    #Негативные проверки
    (".", False),
    ("Vadim", False),
    ("123", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

#----------------list_to_string----------------
@pytest.mark.parametrize('lst, joiner, result', [
    #Позитивные проверки
    (["v","a","d","i","m"], "," , "v,a,d,i,m"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["Город", "Герой"], "-", "Город-Герой"),
    (["Утро", "Вечер"], "День", "УтроДеньВечер"),
    (["ку", "зя"], "", "кузя"),
    #Негативные проверки
    ([], None , ""),
    ([], "," , ""),
    ([], "Kick" , ""),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res =utils.list_to_string(lst, joiner)
    assert res == result 