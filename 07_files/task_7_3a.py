# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


match = 'DYNAMIC'
with open('CAM_table.txt', 'r') as src:    # open file
    vlans = list("")                       # making empty list
    for line in src:
        if match in line:                 # check for matching "DYNAMIC"
            vlans.append(line.replace(match+'     ', "").rstrip())  # add element from strings to the list one by one
vlans.sort()    # sorting list by vlan
for i in vlans:  # print list
    print(i)