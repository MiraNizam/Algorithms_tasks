"""
B. Калькулятор

-- ПРИНЦИП РАБОТЫ --
Решение реализовано на одном стеке, в который добавляются все операнды.
Алгоритм проходит по входным данным в цикле. Встречая операнд, добавляет его в стек, встречая символ операции, достает из
стека два операнда с конца и выполняет операцию.
После вычисления добавляет результат операции в стек последним элементом и продолжает пока не закончатся данные.
Последний элемент стека выводит в результат.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания алгоритма следует, что мы используем структуру данных Стек, это порядок LIFO, что соответствует требованию
обратной польской нотации, где нужно считывать выражение слева направо, но забирая значения с конца.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление и извлечение в стек стоит О(1), а вот проход по входных данным циклом О(n)
Итоговая сложность алгоритма: O(n)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Мы создаем стек, где хранения операндов, это около половины входных данных, но константами мы пренебрегаем,
поэтому итоговая сложность O(n)

-- ID успешной посылки --
https://contest.yandex.ru/contest/22781/run-report/116508986/
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()


def compute_postfix_notation():
    operands = Stack()

    for i in input().split(" "):
        if i in {"+", "-", "/", "*"}:
            x = operands.pop()
            y = operands.pop()

            if i == "+":
                operands.push(y + x)
            elif i == "/":
                operands.push(y // x)
            elif i == "*":
                operands.push(y * x)
            elif i == "-":
                operands.push(y - x)
        else:
            operands.push(int(i))
    return operands.pop()


if __name__ == "__main__":
    print(compute_postfix_notation())
