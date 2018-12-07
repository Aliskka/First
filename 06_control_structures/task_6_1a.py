# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
IP = input('Enter IP-address in format 10.0.1.1: ').split('.')
try:
    for i in range(4):
        IP[i] = int(IP[i])
    if 0 <= IP[0] <= 255 and 0 <= IP[1] <= 255 and 0 <= IP[2] <= 255 and 0 <= IP[3] <= 255:
        if IP[0] == 255 and IP[1] == 255 and IP[2] == 255 and IP[3] == 255:
            print('local broadcast')
        elif IP[0] == 0 and IP[1] == 0 and IP[2] == 0 and IP[3] == 0:
            print('unassigned')
        elif IP[0] < 224:
            print('unicast')
        elif 223 < IP[0] < 240:
            print('multicast')
        elif 239 < IP[0] < 256:
            print('unused')
    else:
        print('Incorrect IPv4 address')

except:
    print('Incorrect IPv4 address')


