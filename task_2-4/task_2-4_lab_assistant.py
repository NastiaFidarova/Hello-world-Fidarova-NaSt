volume = float(input("Введите необходимый объем физического раствора (мл): "))
salt_mass = volume * 0.009
salt_mass_rounded = round(salt_mass, 2)
with open("recipe.txt", "w", encoding="utf-8") as file:
     file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
     file.write("-" * 25 + "\n")
     file.write(f"Общий объем: {volume:.2f} мл\n")
     file.write(f"Масса соли: {salt_mass:.2f} г\n")
     file.write(f"Объем воды:{volume:.2f} мл\n")
print(f"Рецепт усешно сохранен в файл recipe.txt")
print(f"Для приготовления {volume:.2f} мл 0,9% раствора потребуется {salt_mass:.2f} г соли.")