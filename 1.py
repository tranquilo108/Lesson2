# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint

n = int(input('Введите количество монеток: '))
a = []
o = 0
r = 0

for i in range(n):
    a.append(randint(0, 1))

print(a)

for i in a:
    if 1 == i:
        o += 1
    else:
        r += 1

if r < o:
    print(r)
elif r == o:
    print(r, o)
else:
    print(o)
