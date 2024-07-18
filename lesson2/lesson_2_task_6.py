lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

result = []

for element in lst:
    if element <30 and element % 3 ==0:  ## меньше 30, делятся на 3 без остатка.
        result.append(element)

print(result)
