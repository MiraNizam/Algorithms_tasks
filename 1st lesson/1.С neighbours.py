"""
C. Соседи

Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент,
находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.

Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.

В первой строке задано n — количество строк матрицы.
Во второй — количество столбцов m. Числа m и n не превосходят 1000.
В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000.
В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.

Тут отображен пример ввода данных в функцию, работа с матрицей, пока без алгоритмов.
"""


def neighbours():
    rows = int(input())
    columns = int(input())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    #     or
    #  row = sys.stdin.readline().rstrip().split()
    #  matrix.append(row)

    y = int(input())
    x = int(input())

    neighbours = []

    if y + 1 <= rows-1:
        neighbours.append(matrix[y+1][x])
    if y - 1 >= 0:
        neighbours.append(matrix[y - 1][x])
    if x + 1 <= columns-1:
        neighbours.append(matrix[y][x+1])
    if x - 1 >= 0:
        neighbours.append(matrix[y][x-1])

    print(" ".join(map(str, sorted(neighbours))))


if __name__ == '__main__':
    neighbours()
