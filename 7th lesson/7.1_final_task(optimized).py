"""
A. Расстояние по Левенштейну

Расстоянием Левенштейна между двумя строками s и t называется количество атомарных изменений, с помощью которых можно
одну строку превратить в другую. Под атомарными изменениями подразумеваются: удаление одного символа, вставка одного
символа, замена одного символа на другой.

Найдите расстояние Левенштейна для предложенной пары строк.

Выведите единственное число — расстояние между строками.

Формат ввода
В первой строке дана строка s, во второй — строка t. Длины обеих строк не превосходят 1000. Строки состоят из маленьких
латинских букв.

-- ПРИНЦИП РАБОТЫ --
Решение строится на принципах динамического программирования с помощью двумерной динамики.
* Что будет храниться в dp?  в dp хранится матрица, но будем сохранять не всю матрицу, а текущую и предыдущую строки.
* Каким будет базовый случай для задачи? - previous_row[0] = 0
* Каким будет переход динамики? - В каждую следующую клетку переходим выбирая минимальное предыдущее значение.
* Каким будет порядок вычисления данных в массиве? Чтобы посчитать значение в текущей клетке нужно знать предыдущие
значения. То есть при вычислении та часть матрицы, которая находится выше и левее
ячейки (i,j), должна быть уже посчитана.
* Где будет располагаться ответ на исходный вопрос? Искомое значение будет содержаться в previous_row[len_t]

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
в основе решения задачи лежит алгоритм Вагнера-Фишера, который строит матрицу для отслеживания минимальных операций между
подстроками. Мы вычисляем стоимость редактирования 2-х коротких несовпадающих слов(букв) добавляя единицу к текущему
минимальному балансу, если значения не совпадают, иначе, переносим минимальное значение дальше, когда доходим до
последней буквы получаем результат по всему слову.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(st), где s — длина 1-ой строки, t - длина 2-ой строки.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(s), где s — длина строки

-- ID успешной посылки --
https://contest.yandex.ru/contest/25597/run-report/121335704/

"""


def find_levenshtein_distance(s: str, t: str) -> int:  # "обязательно прописать типы данных", у меня вроде не прописаны были типы данных, это имелось ввиду?
    len_s = len(s)
    len_t = len(t)
    previous_row = list(range(len_t + 1))
    current_row = [0] * (len_t + 1)

    for i in range(1, len_s + 1):
        current_row[0] = i
        for j in range(1, len_t + 1):
            if s[i-1] == t[j-1]:
                current_row[j] = previous_row[j - 1]
            else:
                current_row[j] = min(previous_row[j] + 1,  # Удаление
                                 current_row[j - 1] + 1,  # Вставка
                                 previous_row[j - 1] + 1)  # Замена

        previous_row, current_row = current_row, previous_row

    return previous_row[len_t]


def main():
    s = input()
    t = input()
    return find_levenshtein_distance(s, t)


if __name__ == "__main__":
    print(main())
