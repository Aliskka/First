# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
Network, Mask = input('Enter IP-network in format x.x.x.x/x :').split('/') # введение подсети и разделение Network и Mask
Network = Network.split('.') # делаем список из Network
Network = [int(item) for item in Network] # переводим список строк Network в список чисел
Network_output = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
''' # шаблон для вывода Network

Mask = int(Mask) # переводим Mask в число
Mask_bin = '1'*Mask+'0'*(32-Mask) # представляем маску в виде кол-ва бит
Mask_bin = [Mask_bin[:8], Mask_bin[8:16], Mask_bin[16:24], Mask_bin[24:32]] # разделяем по октетам
Mask_bin = [int(item, 2) for item in Mask_bin] # переводим список строк Mask_bin в список чисел
Mask_output = '''
Mask:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
''' # шаблон для вывода Mask

print(Network_output.format(Network[0], Network[1], Network[2], Network[3])) # вывод Network
print(Mask_output.format(Mask_bin[0], Mask_bin[1], Mask_bin[2], Mask_bin[3])) # вывод Mask



















