# Зверюшка со свойствами
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилось на свет новая зверюшка!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено")

    def talk(self):
        print("\nПривет, меня зовут", self.name)


# основная часть
crit = Critter("Бобик")
crit.talk()
print("\nМою звербшку зовут", end=" ")
print(crit.name)
print("\nПопробую изменить имя зверушки на Мурзик...")
crit.name = "Мурзик"
print("\nМою звербшку зовут", end=" ")
print(crit.name)
