# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config):
    with open(config) as file:
        file_as_list = file.read().split('!')   #  делаем охеренный список из конфига, разделяя его "!"
        access = {}
        trunk = {}
        for item in file_as_list:   # ищем access или trunk в элементах списка, разделяем его на элементы и записываем в список номер интерфейса и вланы
            if 'access' in item:
                access.update({item.split()[1]: int(item.split()[8])})
            elif 'trunk' in item:
                vlans = item.split()[10].split(',')
                vlans_int = [int(elem) for elem in vlans]  # переделываем список вланов из строк в цифры
                trunk.update({item.split()[1]: vlans_int})


        return access, trunk

access, trunk = get_int_vlan_map('config_sw1.txt')
print('\n')
print(access)
print('\n')
print(trunk)

