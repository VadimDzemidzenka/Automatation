class Smartphone:
    def __init__(self, brand, model, number):
        self.phone_brand = brand
        self.phone_model = model
        self.phone_number = number

    def sayPhone_brand(self):
        print("марка телефона:", self.phone_brand)
    def sayPhone_model(self):
        print("модель телефона:", self.phone_model)
    def sayPhone_number(self):
        print("абонентский номер:", self.phone_number)
    
