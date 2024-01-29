# Закрытая зверюшка
class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, mood):
        print("Появилось на свет новая зверюшка!")
        self.name = name
        self.__mood = mood

    def talk(self):
        print("\nМеня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mood, "\n")


# основная часть
crit = Critter(name="Бобик", mood="прекрасно")
crit.talk()
