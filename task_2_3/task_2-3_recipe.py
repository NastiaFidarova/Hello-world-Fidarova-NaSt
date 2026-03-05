medium_name = input("Введите название питательной среды: ")
agar_concentration = input('Введите концентрация агар-агара (%): ')
temperature_of_sterilization = input("Укажите температуру стерилизации (градусы цельсия): ")

with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"Среда {medium_name}\n{agar_concentration}\n{temperature_of_sterilization}")

print(f"Файл 'recipe.txt' успешно сформирован!")