# Арсенал героя 3,0
# Демонстрирует работу со списками
# создадим кортеж с несколькими элементами и выведем его с помощью цикла for
inventory = ["меч",
             "кольчуго",
             "щит",
             "целебное снадобье"]
# Выведем все элементы последовательно
print("\nИтак в вашем арсенале:")
for item in inventory:
    print(item)
input("\nНажмите Enter, чтобы продолжить.")

# Найдем длину списка
print("Сейчас в вашем распоряжении", len(inventory), "предмета/-ов.")
input("\nНажмите Enter, чтобы продолжить.")
# проверка на принадлежность к списку с помощью in
if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете")
input("\nНажмите Enter, чтобы продолжить.")

# соединим два кортежа
chest = ("золото", "драгоценные камни")
print("Вы нашли лорец. Вот что в нем есть:")
print(chest)
print("Вы приобщили содержимое ларца к вашему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении:")
print(inventory)
input("Нажмите Enter чтоб продолжить.\n")

# присваиваем значение элементу по индексу
print("Вы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("Теперь ваш арсенал содержит следующие предметы:")
print(inventory)
input("Нажмите Enter чтоб продолжить.\n")

# приписываем значение элементам по срезу индексов
print("За золото и драгоценные камни вы купили магический кристал, способный предсказывать будущее")
inventory[4:6] = ["магический кристал"]
print("Теперь в вашем распоряжении:")
print(inventory)
input("Нажмите Enter чтоб продолжить.\n")

# удаляем элемент
print("В тяжелом бою раздроблен ваш щит.")
del inventory[2]
print("Вот что осталось в арсенале:")
print(inventory)
input("Нажмите Enter чтоб продолжить.\n")

# удаляем срез
print("Воры лишили вас арбалета и кольчуги.")
del inventory[:2]
print("В арсенале теперь только:")
print(inventory)
input("Нажмите Enter чтоб продолжить.\n")