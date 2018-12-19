# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config):
    with open(config) as file:
        file_as_list = file.read().split('!')   #  делаем охеренный список из конфига, разделяя его "!"
        access = {}
        trunk = {}
        for item in file_as_list:   # ищем access или trunk в элементах списка, разделяем его на элементы и записываем в список номер интерфейса и вланы
            if 'access' in item:
                if 'vlan' in item:
                    access.update({item.split()[1]: int(item.split()[8])})
                else:
                    access.update({item.split()[1]: 1})
            elif 'trunk' in item:
                vlans = item.split()[10].split(',')
                vlans_int = [int(elem) for elem in vlans]  # переделываем список вланов из строк в цифры
                trunk.update({item.split()[1]: vlans_int})


        return access, trunk

access, trunk = get_int_vlan_map('config_sw2.txt')
print('\n')
print(access)
print('\n')
print(trunk)
