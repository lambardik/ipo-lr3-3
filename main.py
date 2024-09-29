day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
if 3 <= month <= 5:
  season = "Весна"
elif 6 <= month <= 8:
  season = "Лето"
elif 9 <= month <= 11:
  season = "Осень"
else:
  season = "Зима"
print(f"Дата {day}.{month} относится к {season}.")
