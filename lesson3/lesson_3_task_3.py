from Address import Address
from Mailing import Mailing

to_address = Address("220096", "Минск", "Немига", "3", "130")
from_address = Address("131222", "Гомель", "Дубова", "21", "5")
Mailing = Mailing(to_address, from_address, 75, "№313")

print(f"Отправление {Mailing.track} из {Mailing.from_address.index}, {Mailing.from_address.city},"
      f" {Mailing.from_address.street}, {Mailing.from_address.house} - {Mailing.from_address.apartment} "
      f"в {Mailing.to_address.index}, {Mailing.to_address.city}, {Mailing.to_address.street},"
      f"{Mailing.to_address.house} - {Mailing.to_address.apartment}. Стоимость {Mailing.cost} рублей.")