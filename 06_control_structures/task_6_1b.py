# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
correct_IP = False
while not correct_IP:
    IP = input('Enter IP-address in format 10.0.1.1: ').split('.')
    try:
        for i in range(4):
            IP[i] = int(IP[i])
        if 0 <= IP[0] <= 255 and 0 <= IP[1] <= 255 and 0 <= IP[2] <= 255 and 0 <= IP[3] <= 255:
            if IP[0] == 255 and IP[1] == 255 and IP[2] == 255 and IP[3] == 255:
                print('local broadcast')
                correct_IP = True
            elif IP[0] == 0 and IP[1] == 0 and IP[2] == 0 and IP[3] == 0:
                print('unassigned')
                correct_IP = True
            elif IP[0] < 224:
                print('unicast')
                correct_IP = True
            elif 223 < IP[0] < 240:
                print('multicast')
                correct_IP = True
            elif 239 < IP[0] < 256:
                print('unused')
                correct_IP = True
        else:
            print('Incorrect IPv4 address')
    except:
        print('Incorrect IPv4 address')

