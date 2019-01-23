# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''

def check_ip_addresses(ip_addresses):
    import subprocess
    Dead = []  #  list of dead IP
    Alive = []  #  list of alive IP
    for i in ip_addresses:  #  ping IP and add it to one of lists
        reply = subprocess.run(['ping', '-i', '0.2', '-c', '3', i], stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            Alive.append(i)
        else:
            Dead.append(i)
    return Alive, Dead

Alive, Dead = check_ip_addresses(['8.8.8.8', '195.34.52.12', '2.3.4.5'])

def ip_table(reachability):
    from tabulate import tabulate
    headers = ['Reachable', 'Unreachable']
    print('\n'+tabulate(reachability, headers=headers))

ip_table([Alive, Dead])