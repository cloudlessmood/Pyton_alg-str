"""
Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

a = input("Write set of letters: ")


def counting(a):

    b = set()

    for i in range(len(a) - 1):
        for j in range(i + 1, len(a) + 1):
            b.add(hash(a[i:j]))

    result = len(b) - 1
    return result


result = counting(a)

print(f'String {a} has {result} substrings')