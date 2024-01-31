# Гибель пришельца
class Player(object):
    """Игрок в экшен-игре"""
    def blast(self, enemy):
        print("Игрок стреляет во врага. \n")
        enemy.die()


class Alien(object):
    """Враждебный пришелец инопланетянин"""
    def die(self):
        print("Тяжело дыша, пришелец произносит: 'Ну, вот и все. Спета моя песенка.'\n")


# Основная часть программы
print("\t\tГибель пришельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)
