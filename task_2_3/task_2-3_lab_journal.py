name = input("Введите ФИО исследователя: ")
data = input("Введите дату: ")
name_of_experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")
width = 60  # общая ширина вместе с рамкой
lines = []
lines.append("+" + "-" * (width - 2) + "+") # верхняя граница
header = "| Электронный лабораторный журнал" + " " * (width - len("| Электронный лабораторный журнал") - 1) + "|"
lines.append("+" + "-" * (width - 2) + "+") # разделитель
fields = [
    f"| ФИО исследователя : {name}",
    f"| Дата             : {data}",
    f"| Эксперимент      : {name_of_experiment}"
]
lines.append(field + " " * (width - len(field) - 1) + "|")
lines.append("+" + "-" * (width - 2) + "+") # разделитель 
lines.append("| Вывод:" + " " * (width - len("| Вывод:") - 1) + "|")
max_line_len = width - 4  # оставляем место для "| " и " |" и для отступов от них
words = conclusion.split()
current_line = "| "
for word in words:
    if len(current_line) + len(word) + 1 <= max_line_len:
        current_line += word + " "
else:  
        lines.append(current_line + " " * (width - len(current_line) - 1) + "|")
        current_line = "| " + word + " "
if current_line.strip():
    lines.append(current_line + " " * (width - len(current_line) - 1) + "|")
lines.append("+" + "-" * (width - 2) + "+")

with open("journal.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")

print(f"Файл 'recipe.txt' успешно сформирован!")