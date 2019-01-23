# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def check_ip_addresses(ip_addresses):
    import subprocess
    Dead = []  #  list of dead IP
    Alive = []  #  list of alive IP
    for i in ip_addresses:  #  ping IP and add it to one of lists
        reply = subprocess.run(['ping', '-c', '3', i], stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            Alive.append(i)
        else:
            Dead.append(i)
    print('Alive :', Alive)
    print('Dead :', Dead)

check_ip_addresses(['8.8.8.8', '195.34.52.12', '2.3.4.5'])
