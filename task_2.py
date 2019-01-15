"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = input("Введите любое число - ")

even = 0
odd = 0
even_list = []
odd_list = []

for i in number:
    if int(i) % 2 == 0:
        even += 1
        even_list.append(i)

    elif int(i) % 2 != 0:
        odd += 1
        odd_list.append(i)

    else:
        print('Введено не число')

print(f'Количество четных чисел - {even} {even_list}')
print(f'Количество нечетных чисел - {odd} {odd_list}')
