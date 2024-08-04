def month_to_season(month):
    if month == 12 or 1 <= month < 3:
        print("Зима")
    if 3 <= month <= 5:
        print("Весна")
    if 6 <= month<= 8:
        print("Лето")
    if 9 <= month<= 11:
        print("Осень")
    else: print("Это не число месяца")

try:
    month = int(input("Введите число месяца: "))
    month_to_season(month)
except ValueError: 
    print("Это не число.")