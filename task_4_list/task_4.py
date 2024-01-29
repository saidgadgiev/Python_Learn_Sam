# Рекорды
# Демонстрирует списочные методы
scores = []
choice = None
while choice != "0":
    print(
        """
        Рекорды
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорд
        3 - Удалить рекорд
        4 - Сортировать список
        """
    )
    choice = input("Ваш выбор: ")
    print()
    # Выход
    if choice == "0":
        print("До свидания.")
    # Вывод лучших результатов на экран
    elif choice == "1":
        print("Рекорды")
        for score in scores:
            print(score)
    # Добавление рекорда
    elif choice == "2":
        score = int(input("Впишите свой рекорд: "))
        scores.append(score)
    # Удаление рекорда
    elif choice == "3":
        score = int(input("Какой изх рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат", score, "не содержит в списке рекордов.")
    # сортировка рекордов
    elif choice == "4":
        scores.sort(reverse=True)
    # Не понятный пользовательский ввод
    else:
        print("Извините, в меню нет пункта", choice)

