# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan  = input('Enter vlan number: ')  # ask for vlan number
match = 'DYNAMIC'
with open('CAM_table.txt', 'r') as src:    # open file
    vlans = list("")                       # making empty list
    for line in src:
        if match in line:                 # check for matching "DYNAMIC"
            vlans.append(line.replace(match+'     ', "").rstrip())  # add element from strings to the list one by one
vlans.sort()    # sorting list by vlan
for i in vlans:  # print list
    if vlan in i:
        print(i)