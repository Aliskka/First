# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
name = str(argv[1:]).strip('[]').strip("'")
with open(name, 'r') as src, open('config_sw1_cleared.txt', 'w') as dest:
    for line in src:
        for word in ignore:
            if word in line:
                break
        else:
            dest.write('\n' + (line.rstrip()))


