# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


def search_index(firstnum, secondnum, num):
    mylist = [randint(firstnum, secondnum) for i in range(num)]
    print("Созданый массив:", mylist)
    indexes = [i for i, v in enumerate(mylist) if minnum <= v <= maxnum]
    result = []
    i = len(indexes)
    while i:
        i -= 1
        result.append(mylist.pop(indexes[i]))
    return indexes


firstnum = int(input('В списке будут чмсла от?: '))
secondnum = int(input('И до?: '))
num = int(input('Сколько элементов будет в списке?: '))
minnum = int(input('Будем искать индексы чисел от?: '))
maxnum = int(input('И до?: '))

print(search_index(firstnum, secondnum, num))
