# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
vlan = 'VLAN number: '  # template question for access
vlans = 'allowed VLANs: '  # template question for trunk

mode_template = { 'access':access_template, 'trunk':trunk_template}  # making mode dictionary depending of interface mode
vlan_template = { 'access':vlan, 'trunk':vlans}  # making vlan(s) dictionary depending of interface mode

if_mode = input('Enter interface mode (access/trunk): ')  # entering interface mode
if_number = input('Enter interface type and number: ')  # entering interface type and number

if_vlan = input('Enter {}'.format(vlan_template[if_mode]))  # entering vlan(s)

print('\n' + '-' * 30)  #just separating line
print('interface {}'.format(if_number))  # printing interface
print('\n'.join(mode_template[if_mode]).format(if_vlan))  # printing settings of interface