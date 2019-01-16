# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology
full_topology = {**parse_cdp_neighbors('sh_cdp_n_sw1.txt'), **parse_cdp_neighbors('sh_cdp_n_r1.txt'), **parse_cdp_neighbors('sh_cdp_n_r2.txt'), **parse_cdp_neighbors('sh_cdp_n_r3.txt') }
print(full_topology)
for key in list(full_topology):  # delete matches any_key=any_value
    for item in list(full_topology):
        if key == full_topology[item]:
            del(full_topology[key])
draw_topology(full_topology)