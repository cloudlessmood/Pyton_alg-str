"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы."""

import random


orig_list = random.sample(range(50), 10)


def merge_sorting(orig_list):
    if len(orig_list) < 2:
        return orig_list

    a = merge_sorting(orig_list[:len(orig_list)//2])
    b = merge_sorting(orig_list[len(orig_list)//2:len(orig_list)])

    i=j=0
    new = []

    while i < len(a) or j < len(b):
        if not i < len(a):
            new.append(b[j])
            j += 1

        elif not j < len(b):
            new.append(a[i])
            i += 1

        elif a[i] < b[j]:
            new.append(a[i])
            i += 1

        else:
            new.append(b[j])
            j += 1

    return new


print("Original list - ", orig_list)
print("Sprting by merging - ", merge_sorting(orig_list))
