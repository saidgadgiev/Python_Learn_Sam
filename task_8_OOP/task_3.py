# Классово верная зверюшка
class Critter(object):
    """Виртуальный питомец"""
    total = 0

    @staticmethod
    def status():
        print("\nВсего зверюшек сейчас", Critter.total)

    def __init__(self, name):
        print("Появилось на свет новая зверюшка!")
        self.name = name
        Critter.total += 1


# основная часть
print("Нахожу значение атрибута класса Critter.total:", end=" ")
print(Critter.total)
print("\nСоздаю зверюшек.")
crit1 = Critter("Зверюшка 1")
crit2 = Critter("Зверюшка 2")
crit3 = Critter("Зверюшка 3")
Critter.status()
print("\nОбращаюсь к атрибутам класса через объект:", end=" ")
print(crit1.total)
