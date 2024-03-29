# Переводчик с гикского на русский
# Демонстрируем использование словарей
geek = {"404": "Не знать, не владеть информацией. От сообщения об ошибке 404 'Страница не найдена'.",
    "Googling": "'Гугление', поиск в Сети сведений о ком-либо.",
    "Keyboard Plaque": "Мусор, который скапливается в клавиатуре компьютера",
    "Link rot": "Процесс устранения гиперссылок на веб-страницах",
    "Uninstalled": "Об увольнении кого-либо. Особенно популярно на рубеже 1990-2000-х годов."}
choice = None
while choice != "0":
    print(
        """
        Переводчик с гикского на русский
        0 - Выйти
        1 - Найти толкование термина
        2 - Добавить в термин
        3 - Изменить толкование
        4 - Удалить термин
        """
    )
    choice = input("Ваш выбор: ")
    print()
    # Выход
    if choice == "0":
        print("До свидание")
    # Поиск толкования
    elif choice == "1":
        term = input("Какой термин вы хотите перевести? ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "озночает", definition)
        else:
            print("\nУвы этот термин мне не знаком:", term)
    elif choice == "2":
        term = input("Какой термин вы хотите добавить? ")
        if term not  in geek:
            definition = input("\nВпишите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term, "добавлен в словарь.")
        else:
            print("\nТакой термин уже есть! Попробуйте изменить его толкование.")
    # новое толкование известного термина
    elif choice == "3":
        term = input("Какой термин вы хотите переопределить? ")
        if term in geek:
            definition = input("Впишите ваше толкование: ")
            geek[term] = definition
            print("\nТермин", term, "переопределен.")
        else:
            print("\nТакого термина пока нет! Попробуйте добавить его в словарь.")
    # удаление термина вместе с его толкованием
    elif choice == "4":
        term = input("Какой термин вы хотите удалить? ")
        if term in geek:
            del geek[term]
            print("\nТермин", term, "удален.")
        else:
            print("\nНичем не могу помочь. Термина", term, "нет в словаре.")
    # Не понятный пользовательский ввод
    else:
        print("Извините, в меню нет пункта", choice)
