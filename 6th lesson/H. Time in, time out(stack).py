"""
H. Время выходить

Вам дан ориентированный граф. Известно, что все его вершины достижимы из вершины s=1. Найдите время входа и выхода при
обходе в глубину, производя первый запуск из вершины s. Считайте, что время входа в стартовую вершину равно 0. Соседей
каждой вершины обходите в порядке увеличения номеров.

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 2⋅ 105) и рёбер (0 ≤ m ≤ 2 ⋅ 105). В каждой из следующих m строк записаны
рёбра графа в виде пар (from, to), 1 ≤ from ≤ n — начало ребра, 1 ≤ to ≤ n — его конец. Гарантируется, что в графе
нет петель и кратных рёбер.

Формат вывода
Выведите n строк, в каждой из которых записана пара чисел tini, touti — время входа и выхода для вершины i.

"""
from collections import defaultdict


def adjacency_list(edge_list):
    adjacency_list = defaultdict(list)

    for u, v in edge_list:
        adjacency_list[u].append(v)
    return adjacency_list


def dfs_time_in_out(n, adjacency_dict, s=1):
    color = ["white"] * (n + 1)
    time = 0
    entry = [None] * (n + 1)  # обновляется, когда вершина красится в серый цвет
    leave = [None] * (n + 1)  # обновляется, когда перекрашивается в чёрный

    stack = [s]

    while stack:
        v = stack.pop()

        if color[v] == 'white':
            entry[v] = time
            time += 1
            color[v] = 'gray'
            stack.append(v)

            for w in sorted(adjacency_dict[v], reverse=True):
                if color[w] == 'white':
                    stack.append(w)
        elif color[v] == 'gray':
            leave[v] = time
            time += 1
            color[v] = 'black'

    for i in range(1, n + 1):
        print(entry[i], leave[i])


def main():
    n, m = tuple(map(int, (input().split(" "))))  # number vertex, number edge
    edge_list = [list(map(int, (input().split(" ")))) for _ in range(m)]

    adjacency_dict = adjacency_list(edge_list)
    dfs_time_in_out(n, adjacency_dict, s=1)


if __name__ == "__main__":
    main()