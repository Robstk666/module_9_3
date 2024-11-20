# Исходные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для вычисления разницы длин строк из first и second (если их длины не равны)
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк в одинаковых позициях без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))  # Преобразуем генератор в список для вывода
print(list(second_result))