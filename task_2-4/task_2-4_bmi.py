weight = float(input("Введите ваш вес (кг): "))
hight_cm = float(input("Введите ваш рост (см): "))
hight_m = hight_cm / 100 
bmi = weight / (hight_m ** 2) # расчитываем индекс массы тела по формуле 
print("\n--- Отсчет о состоянии здоровья ---")
print(f"Рост:\t{hight_cm:.1f} см")
print(f"Вес:\t{weight:.1f} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")