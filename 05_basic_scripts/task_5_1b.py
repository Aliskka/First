# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


#IP, Mask = input('Enter IP-address in format x.x.x.x/x :').split('/')  # введение подсети и разделение Network и Mask
#IP = IP.split('.')  # делаем список из Network
#IP = [bin(int(item)) for item in IP]  # переводим список строк Network в список чисел

from sys import argv  # импорт argv из модуля sys
IP, Mask = argv[1].split('/')  # передача аргумента подсети и разделение Network и Mask

IP = IP.split('.')  # делаем список из Network
IP = [bin(int(item)) for item in IP]  # переводим список строк Network в список чисел

Mask = int(Mask)  # переводим Mask в число
Mask_str = '1'*Mask+'0'*(32-Mask)  # представляем маску в виде кол-ва бит
Mask_str = [Mask_str[:8], Mask_str[8:16], Mask_str[16:24], Mask_str[24:32]]  # разделяем по октетам
Mask_int = [int(item, 2) for item in Mask_str]  # переводим список строк Mask_bin в список чисел

Network = [1, 2, 3, 4]  # создаем список Network с рандомными значениями
for item in range(4):
    Network[item] = (int(Mask_str[item], 2)&int(IP[item], 2))  # делаем логическое "И" между бинарными IP и маской

Network_output = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''  # шаблон для вывода Network

Mask_output = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''  # шаблон для вывода Mask

print(Network_output.format(Network[0], Network[1], Network[2], Network[3]))  # вывод Network

print('Mask:\n/' + str(Mask) +
Mask_output.format(Mask_int[0], Mask_int[1], Mask_int[2], Mask_int[3]))  # вывод Mask