from smartphone import Smartphone

catalog = ([])

phone1 = Smartphone("Apple", "15 pro", "+3752926013221")
phone2 = Smartphone("Samsung", "Galaxy","+3752926013221")
phone3 = Smartphone("Xiaomi", "Redmi Note 13", "+3752926013221")
phone4 = Smartphone("POCO", "F6 Pro", "+3752926013222")
phone5 = Smartphone("HONOR", "200 Lite", "+3752926013223")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print("brand", "model", "number")