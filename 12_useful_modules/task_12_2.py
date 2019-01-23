# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''

def check_ip_availability(ip_addresses):
    import subprocess
    Dead = []  #  list of dead IP
    Alive = []  #  list of alive IP
    for i in ip_addresses:
        if '-' in i:  #  check is it range of IP-address or single IP
            octets = i.replace('-', '.').split('.')  #  devide string for list of octets
            count = int(octets[3])
            while count != int(octets[-1])+1:  #  ping one IP from range and add it to one of lists
                ip = octets[0]+'.'+octets[1]+'.'+octets[2]+'.'+str(count)
                reply = subprocess.run(['ping', '-i', '0.2', '-c', '3', ip], stdout=subprocess.DEVNULL)
                count+=1
                if reply.returncode == 0:
                    Alive.append(ip)
                else:
                    Dead.append(ip)
        else:  #  ping single IP and add it to one of lists
            reply = subprocess.run(['ping', '-i', '0.2', '-c', '3', i], stdout=subprocess.DEVNULL)
            if reply.returncode == 0:
                Alive.append(i)
            else:
                Dead.append(i)
    print('Alive :', Alive)
    print('Dead :', Dead)

check_ip_availability(['8.8.8.8', '195.34.52.12-195.34.52.20', '1.2.3.4-10'])