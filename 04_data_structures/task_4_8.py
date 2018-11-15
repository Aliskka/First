# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = '192.168.3.1'
IP = IP.split('.') #точкой разделяем строку
IP[0] = int(IP[0])
IP[1] = int(IP[1])
IP[2] = int(IP[2])
IP[3] = int(IP[3])
print(IP)
type(IP[0])

result = '''
{:<8}  {:<8}  {:<8}  {:<8} 
{:08b}  {:08b}  {:08b}  {:08b}
'''# шаблон для вывода значений

print(result.format(IP[0], IP[1], IP[2], IP[3], IP[0], IP[1], IP[2], IP[3]))
