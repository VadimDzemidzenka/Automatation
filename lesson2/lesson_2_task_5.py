def month_to_season(month):
    if month == 1 or month == 2 or month == 12:
        return("зима")
    elif month == 3 or month == 4 or month == 5:
        return("весна")
    elif month == 6 or month == 7 or month == 8:
        return("лето")
    elif month == 9 or month == 10 or month == 11:
        return("осень")
    else:
        return("Укажите правильный номер месяца")
print(month_to_season(int(input('Введите номер месяца '))))