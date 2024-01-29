# Программа, в которой случайное число от 1 до 100 загадывает человек, а отгадывает компьютер
import random

my_number = int(input('Введите число от 1 до 100 -> '))
finish = True
count_attempts = 0  # счетчик попыток
comp_number = random.randint(1, 100)  # случайное число введенное компьютером
min = 0
max = 100
while finish:
    count_attempts += 1
    if my_number == comp_number: # 50, 40
        print("Число отгаданно, это ", comp_number)
        print(f"Было использованно {count_attempts} попыток")
        finish = False
    elif my_number > comp_number:  # если загаданное число больше
        min = comp_number
        comp_number = random.randint(min, max)
    elif my_number < comp_number:
        max = comp_number
        comp_number = random.randint(min, max)

