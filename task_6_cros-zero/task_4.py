# Доступ отовсюду
def read_global():
    print("В области видимости функции read_global() значение value равно", value)


def shadow_global():
    value = -10
    print("В области видимости функции shadow_global() значение value равно", value)


def change_global():
    global value
    value = -10
    print("В области видимости функции change_global() значение value равно", value)


# Основная часть
# value - глобальная переменная, потому что сейчас мы находимся в глобальной области видимости
value = 10
print("В глобальной области видимости значение переменой value сейчас стало равным", value, "\n")
read_global()
print("Вернемся в глобальную область видимости. Значение value по прежнему равно", value, "\n")
shadow_global()
print("Вернемся в глобальную область видимости. Значение value по прежнему равно", value, "\n")
change_global()
print("Вернемся в глобальную область видимости. Значение value изменилось на", value, "\n")
