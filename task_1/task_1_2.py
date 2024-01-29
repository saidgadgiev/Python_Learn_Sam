# Написать программу, которая бы "подбрасывала" условную монету 100
# раз и сообщала, сколько раз выпал орел, а сколько - решка
import random
count_heads = 0  # счетчик орла
count_tails = 0  # счетчик решки
heads, tails = 0, 1  # орел это 0, а решка - 1
count_attempts = 0  # счетчик попыток
while count_attempts <= 100:
    numbs = random.randrange(2)
    count_attempts += 1  # Увеличение счетчика попыток на 1
    if numbs == 0:
        count_heads += 1
    else:
        count_tails += 1

print(f'Из 100 попыток орел выпал {count_heads} раз, а решка {count_tails} раз')

