day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

if month < 1 or month > 12:
    print("Некорректный месяц. Введите число от 1 до 12.")
    month = int(input("Введите месяц: "))

if day < 1:
    print("Некорректный день. Введите число от 1 до 31.")
    day = int(input("Введите день: "))

if month in [4, 6, 9, 11] and day > 30:
    print(f"В {month} месяце не может быть больше 30 дней. Введите число от 1 до 30.")
    day = int(input("Введите день: "))
elif month == 2 and day > 29:
    print("В феврале не может быть больше 29 дней. Введите число от 1 до 29.")
    day = int(input("Введите день: "))
elif day > 31:
    print("Некорректный день. Введите число от 1 до 31.")
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
