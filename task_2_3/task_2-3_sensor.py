name = input("Введите имя опертора: ")
current_pressure = input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "w", encoding="utf-8") as sensor:
    sensor.write(f"ОПЕРАТОР \t {name} \nЗНАЧЕНИЕ \t {current_pressure}")

print("Данные успешно сохранены в sensor_log.txt")