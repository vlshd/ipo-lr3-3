day = int(input("Введите день: ")) # Запрашиваем ввод дня
month = int(input("Введите месяц: ")) # Запрашиваем ввод месяца

if (month == 3 and day >= 1 and day <= 31) or (month == 4 and day >= 1 and day <= 31) or (month == 5 and day <= 31): # Делаем условие, чтобы вводимые день и месяц были Весна
        print("Весна")
if (month == 6 and day >= 1) or (month == 7 and day >= 1 and day <= 31) or (month == 8 and day <= 31): # Делаем условие, чтобы вводимые день и месяц были Лето
        print("Лето")
if (month == 9 and day >= 1) or (month == 10 and day >= 1 and day <= 31) or (month == 11 and day <= 30): # Делаем условие, чтобы вводимые день и месяц были Осень
        print("Осень")
if (month == 12 and day >= 1) or (month == 1 and day >= 1 and day <= 31) or (month == 2 and day <= 28): # Делаем условие, чтобы вводимые день и месяц были Зима
        print("Зима") 
