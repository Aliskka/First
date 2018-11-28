# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]
#  ---------------------------------------------------
num = int(input("Enter number from num_list (2, 7, 10, 11, 15, 30, 100) for it's index: "))  # ask for entering number
index_reverse_list = num_list[::-1].index(num)  #  reverse and understand undex of number
print(len(num_list) - index_reverse_list - 1)  #  lenth of num_list minus word index and minus one

#  ---------------------------------------------------

word = input("Enter word from word_list (python, ruby, perl) for it's index: ")  # ask for entering word
index_reverse_word = word_list[::-1].index(word)  #  reverse and understand index of word
print(len(word_list) - index_reverse_word - 1)  #  lenth of word_list minus word index and minus one