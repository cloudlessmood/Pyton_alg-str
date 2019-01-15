"""Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

number = str(input("Введите любое число - "))

revers = []


def reverse(number):

    if len(number) == 0:
        return ''.join(revers)

    else:
        revers.append(number[-1])
        number = list(number[:-1])
        print(reverse(number))


print(reverse(number))
