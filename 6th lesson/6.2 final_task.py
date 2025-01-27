"""
B. Железные дороги

В стране X есть n городов, которым присвоены номера от 1 до n. Столица страны имеет номер n. Между городами проложены
железные дороги.

Однако дороги могут быть двух типов по ширине полотна. Любой поезд может ездить только по одному типу полотна.
Условно один тип дорог помечают как R, а другой как B. То есть если маршрут от одного города до другого имеет как дороги
типа R, так и дороги типа B, то ни один поезд не сможет по этому маршруту проехать. От одного города до другого можно
проехать только по маршруту, состоящему исключительно из дорог типа R или только из дорог типа B.

Но это ещё не всё. По дорогам страны X можно двигаться только от города с меньшим номером к городу с большим номером.
Это объясняет большой приток жителей в столицу, у которой номер n.

Карта железных дорог называется оптимальной, если не существует пары городов A и B такой, что от A до B можно добраться
как по дорогам типа R, так и по дорогам типа B. Иными словами, для любой пары городов верно, что от города с меньшим
номером до города с бОльшим номером можно добраться по дорогам только какого-то одного типа или же что маршрут построить
вообще нельзя. Выясните, является ли данная вам карта оптимальной.

Формат ввода
В первой строке дано число n (1 ≤ n ≤ 5000) — количество городов в стране. Далее задана карта железных дорог в следующем
формате.

Карта задана n-1 строкой. В i-й строке описаны дороги из города i в города i+1, i+2, ..., n. В строке записано n - i
символов, каждый из которых либо R, либо B. Если j-й символ строки i равен «B», то из города i в город i + j идет дорога
типа «B». Аналогично для типа «R».

Формат вывода
Выведите «YES», если карта оптимальна, и «NO» в противном случае.


-- ПРИНЦИП РАБОТЫ --
строится на алгоритме DFS, который проверяет существует ли цикл в направленном графе. На основе карты ж/д дорог мы
строим лист смежности.
Из: ["BBB", "RB", "B"]
Получаем: [[], [0, 2], [0], [0, 1, 2]] если R, то прокладываем ребро от текущего города к городу-цели, если В,
то прокладываем ребро в обратном направлении. Обходим граф поиском в глубину, чтобы найти циклы.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
В основе решения лежит обход графов в глубину, алгоритм обходит все достижимые вершины графа, если во время обхода
находится соседняя вершина, которая в состоянии 1, то это указывает на наличие цикла и задача завершается, если нет,
то обход продолжается до последнего элемента.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(∣E∣ + ∣V∣), где ∣E∣ — количество рёбер в графе, а ∣V∣ — количество вершин.
O(n^2), где  n - количество городов.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(∣V∣), где ∣V∣ — количество вершин.
O(n), где  n - количество городов.

-- ID успешной посылки --
https://contest.yandex.ru/contest/25070/run-report/120528026/

"""
WHITE = 0
GRAY = 1
BLACK = 2


def dfs(vertex, adjacency, components):
    stack = [vertex]
    while stack:
        v = stack[-1]
        if components[v] == WHITE:
            components[v] = GRAY
            for neighbor in adjacency[v]:
                if components[neighbor] == WHITE:
                    stack.append(neighbor)
                elif components[neighbor] == GRAY:
                    return True
        else:
            components[v] = BLACK
            stack.pop()
    return False


def is_optimal(n, rail_map):
    city_count = n - 1
    adjacency = [[] for _ in range(n)]

    for i in range(city_count):
        for j in range(city_count - i):
            target_city = i + j + 1
            if rail_map[i][j] == "R":
                adjacency[i].append(target_city)
            elif rail_map[i][j] == "B":
                adjacency[target_city].append(i)
    components = [WHITE] * len(adjacency)
    for vertex in range(len(adjacency)):
        if components[vertex] == WHITE and dfs(vertex, adjacency, components):
            return "NO"
    return "YES"


def main():
    n = int(input())
    rail_map = [input() for _ in range(n-1)]
    return is_optimal(n, rail_map)


if __name__ == "__main__":
    print(main())

