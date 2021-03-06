# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

vlans1 = command1.split()[-1].split(',')
vlans2 = command2.split()[-1].split(',')
print("-------------------------------------------------------------------------")
vlans_int1 = [int(i) for i in vlans1]
vlans_int2 = [int(i) for i in vlans2]
vlans1.sort()
vlans2.sort()
print(vlans_int1)
print(vlans_int2)
print("-------------------------------------------------------------------------")
vlans_int1 = set(vlans_int1)
vlans_int2 = set(vlans_int2)
vlans = (vlans_int1.intersection(vlans_int2))
vlans = list(vlans)
print(vlans)
