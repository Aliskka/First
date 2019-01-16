# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def parse_cdp_neighbors(output_file):
    source = ()
    dest = ()
    result = {}
    with open(output_file) as file:  # defining device from which the command is made
        for line in file:
            if 'cdp' in line:
                device = line.replace('>show cdp neighbors', '').strip()
    with open(output_file) as file:  # adding cdp neighbors to dictionary line by line
        for line in file:
            if ('Eth' or 'Fa') in line:
                source = (device, line.split()[1]+line.split()[2])
                dest = (line.split()[0], line.split()[-2]+line.split()[-1])
                result[source] = dest
    return(result)

if __name__ == "__main__":
    print(parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt'))
