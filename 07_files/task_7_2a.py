# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
name = str(argv[1:]).strip('[]').strip("'")  # entering file name as argument
with open(name, 'r') as f:  #  open file
    for line in f:
        for word in ignore:            #  check for words should be exapted
            if word in line:
                break
        else:
            if not line.startswith('!'):   # remove '!' in lines
                print(line.rstrip())

