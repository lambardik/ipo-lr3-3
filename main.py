day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

if month < 1 or month > 12:
    print("Некорректный месяц. Введите число от 1 до 12.")
    month = int(input("Введите месяц: "))

if day < 1 or day > 31:
    print("Некорректный день. Введите число от 1 до 31.")
    day = int(input("Введите день: "))

if month == 2 and day > 29:
    print("В феврале может быть до 29 дней в високосный год. Введите число от 1 до 29.")
    day = int(input("Введите день: "))

if 3 <= month <= 5:
    season = "Весна"
elif 6 <= month <= 8:
    season = "Лето"
elif 9 <= month <= 11:
    season = "Осень"
else:
    season = "Зима"

print(f"Дата {day}.{month} относится к {season}.")
