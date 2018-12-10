# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('ospf.txt', 'r') as f:
    for line in f:
        line = line.split()
        line.remove('via')
        line[0] = 'OSPF'
        line[2] = line[2].strip('[]')
        line[3] = line[3].strip(',')
        line[4] = line[4].strip(',')
        ip_template = '''
        {:23} {:23}
        {:23} {:23}
        {:23} {:23}
        {:23} {:23}
        {:23} {:23}
        {:23} {:23}
                   '''
        print(ip_template.format("Protocol:", line[0], "Prefix:", line[1], "AD/Metric:", line[2],
                                 "Next-Hop:", line[3], "Last update:", line[4], "Outbound Interface:",
                                 line[5]))




