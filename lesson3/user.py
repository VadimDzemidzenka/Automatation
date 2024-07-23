class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirst_name(self):
        print("ИМЯ:", self.first_name)
    def sayLast_name(self):
        print("ФАМИЛИЯ:", self.last_name)
    def sayFirst_Last_name(self):
        print("ИМЯ и ФАМИЛИЯ:", self.first_name, self.last_name)
