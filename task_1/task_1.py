# Отгадай число
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число, и компьютер говорит,
# предложение больше или меньше чем загаданное число.
# или попало в точку

import random
print("\tДобро пожаловать в игру 'Отгадай число'!")
print('\nЯ загадал натуральное число из диапазона от 1 до 100.')
print('Попытайся отгадать его за минимальное число попыток.\n')
#  начальные значения
the_number = random.randint(1, 100)
guess = None
tries = 1

# цикл отгадывания
while guess != the_number:
    guess = int(input("Ваше предложение: "))
    if guess > the_number:
        print("Меньше...")
    else:
        print("Больше")
    tries += 1
print("Вам удалось отгадать число! Это в самом деле", the_number)
print("Вы затратили на отгадывание всего лишь ", tries, " попыток!\n")
