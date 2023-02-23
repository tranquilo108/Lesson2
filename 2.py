# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# a = 30
# b = 14
a = 44
b = 420
list_of_a = []
list_of_b = []
for i in range(1, a + 1):
    if a - i > 0:
        list_of_a.append(i)

for i in range(1, b + 1):
    if b % i == 0:
        list_of_b.append(i)

for i in range(len(list_of_a)):
    for j in range(len(list_of_a)):
        if i * j == b and i + j == a:
            print(i, j)


#print(list_of_b, list_of_a)