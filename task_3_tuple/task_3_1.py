# Арсенал героя
# Демонстрирует создание кортежа
inventory = ()  # Создадим пустой кортеж
# Рассмотрим его как условие
if not inventory:
    print("Вы безоружны.")
input("\nНажмите Enter, чтобы продолжить.")
inventory = ("меч",
             "кольчуго",
             "щит",
             "целебное снадобье")
# Выведем этот кортеж на экран
print("\nСодержимое кортежа:")
print(inventory)
# Выведем все элементы последовательно
print("\nИтак в вашем арсенале:")
for item in inventory:
    print(item)