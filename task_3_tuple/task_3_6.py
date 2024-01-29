# Анаграммы (Word Jumble)

# Компьютер выбирает какое-либо слово и хаотично переставляет буквы
# Задача игрока - восстановить исходное слово
import random
score = 3
# Создадим последовательность слов, из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word

# Создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble = word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
"""
        Добро пожаловать в игру 'Анаграммы'!
    Надо переставить буквы так, чтобы получилось осмысленное слово.
    (Для выхода нажмите Enter, не вводя своей версии.)
"""
print("Вот анаграмма:", jumble)

guess = input(f"\nПопробуйте отгадать исходное слово из возможных вариантов {WORDS}: ")
while guess != correct and guess != "":
    print("К сожалению вы не правы.")
    score -= 1
    guess = input("Попробуйте отгадать исходное слово: ")
if guess == correct:
    print("Да, именно так! Вы отгадали! У вас ", score, "балла\n")
print("Спасибо за игру.")
