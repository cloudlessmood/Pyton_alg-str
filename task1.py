"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random

orig_list = [random.randint(-100, 100) for _ in range(10)]


def sorting(orig_list):

    for i in range(len(orig_list)):
        for j in range(len(orig_list)-1, i, -1):
            if orig_list[j] < orig_list[j - 1]:
                orig_list[j], orig_list[j - 1] = orig_list[j - 1], orig_list[j]

    return orig_list


print("Исходный список - ", orig_list)
print("Отсортированный методом пузырька - ", sorting(orig_list))
