def vremena_goda(day, month):
    if (month == 3 and day >= 1 and day <= 31) or (month == 4 and day >= 1 and day <= 31) or (month == 5 and day <= 31): # Делаем условие, чтобы вводимые день и месяц были Весна
        return "Весна"
    elif (month == 6 and day >= 1) or (month == 7 and day >= 1 and day <= 31) or (month == 8 and day <= 31): # Делаем условие, чтобы вводимые день и месяц были Лето
        return "Лето"
    elif (month == 9 and day >= 1) or (month == 10 and day >= 1 and day <= 31) or (month == 11 and day <= 30): # Делаем условие, чтобы вводимые день и месяц были Осень
        return "Осень"
    elif (month == 12 and day >= 1) or (month == 1 and day >= 1 and day <= 31) or (month == 2 and day <= 28): # Делаем условие, чтобы вводимые день и месяц были Зима
        return "Зима" 

day = int(input("Введите день: ")) # Запрашиваем ввод дня
month = int(input("Введите месяц: ")) # Запрашиваем ввод месяца
season = vremena_goda(day, month) # Присваиваем переменной условия функции времена года
print(f"Время года: {season}") # Выводим время года