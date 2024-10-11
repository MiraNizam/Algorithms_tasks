"""
H. Поле с цветочками

Черепаха Кондратина путешествует по клетчатому полю из n строк и m столбцов. В каждой клетке либо растёт цветочек,
либо не растёт. Кондратине надо добраться из левого нижнего в правый верхний угол и собрать как можно больше цветочков.

Помогите ей с этой сложной задачей и определите, какое наибольшее число цветочков она сможет собрать при условии,
что Кондратина умеет передвигаться только на одну клетку вверх или на одну клетку вправо за ход.

Формат ввода
В первой строке даны размеры поля n и m (через пробел). Оба числа лежат в диапазоне от 1 до 1000. В следующих n
строках задано поле. Каждая строка состоит из m символов 0 или 1, записанных подряд без пробелов, и завершается
переводом строки. Если в клетке записана единица, то в ней растёт цветочек.

Формат вывода
Выведите единственное число — максимальное количество цветочков, которое сможет собрать Кондратина.

"""


def field(n, m, matrix):
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            flower_count = int(matrix[i][j])
            if i == 0 and j == 0:
                dp[i][j] = flower_count
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + flower_count
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + flower_count
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + flower_count
    return dp[n-1][m-1]


def main():
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    matrix.reverse()
    result = field(n, m, matrix)
    print(result)


if __name__ == "__main__":
    main()
