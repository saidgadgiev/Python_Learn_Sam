# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choice = None
while choice != "0":
    print(
        """
        0 - Выйти
        1 - Показатьт рекорды
        2 - Добавить рекорд
        """
    )
    choice = input("Ваш выбор: ")
    print()
    # Выход
    if choice == "0":
        print("До свидания.")
    # Вывод таблицы рекордов
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry  # результат, имя
            print(name, "\t", score)
    # Добавляем результат
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score, name)  # Добавление в список
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # в списке остается только 5 рекордов

    # Непонятный пользовательский ввод
    else:
        print("Извините, в меню нет пункта", choice)

