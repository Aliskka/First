# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route
ospf_route = ospf_route.split()
ospf_route.remove('via')
ospf_route[0] = 'OSPF'
ospf_route[2] = ospf_route[2].strip('[]')
ospf_route[3] = ospf_route[3].strip(',')
ospf_route[4] = ospf_route[4].strip(',')

print(ospf_route)


ip_template = '''
{:23} {:23}
{:23} {:23}
{:23} {:23}
{:23} {:23}
{:23} {:23}
{:23} {:23}
           '''

print(ip_template.format("Protocol:", ospf_route[0], "Prefix:", ospf_route[1], "AD/Metric:", ospf_route[2], "Next-Hop:", ospf_route[3], "Last update:", ospf_route[4], "Outbound Interface:", ospf_route[5]))

