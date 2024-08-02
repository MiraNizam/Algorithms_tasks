"""
A. Генератор скобок

Сгенерировать все ПСП длины 2n в алфавитном порядке —– алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.
Написать программу, которая по-заданному n выведет все ПСП в нужном порядке.

Рассмотрим второй пример. Надо вывести ПСП из четырёх символов. Таких всего две:

(())
()()
(()) идёт раньше ()(), так как первый символ у них одинаковый, а на второй позиции у первой ПСП стоит (, который идёт раньше ).
Формат ввода
На вход функция принимает n — целое число от 0 до 10.

Формат вывода
Функция должна напечатать все возможные скобочные последовательности заданной длины в алфавитном (лексикографическом) порядке.

"""
n = int(input())*2


def bracket_sequence_generator(n, sequence="", counter=0):
    if n == 0:
        if counter == 0:
            print(sequence)
    else:
        if counter > 0:
            bracket_sequence_generator(n-1, sequence + "(", counter + 1)
            bracket_sequence_generator(n-1, sequence + ")", counter - 1)
        else:
            bracket_sequence_generator(n-1, sequence + "(", counter + 1)


if __name__ == "__main__":
    bracket_sequence_generator(n)