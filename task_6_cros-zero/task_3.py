# День рождение
def birthday1(name, age):
    print("С днем рождения.", name, "!", "Вам сегодня исполняется", age, ", не так ли?\n")
# параметры со значениями по умолчанию


def birthday2(name = "товарищ Иванов", age = 1):
    print(print("С днем рождения.", name, "!", "Вам сегодня исполняется", age, ", не так ли?\n"))


# birthday1("товарищ Иванов", 1)
# birthday1(1, "товарищ Иванов")
birthday2()
# birthday2(name="Катя")
# birthday2(age=12)
# birthday2(name="Катя", age=12)
# birthday2("Катя", 12)