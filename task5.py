"""Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

a = input("Введите букву русского алфавита: ")
b = input("Введите еще одну букву русского алфавита: ")

alphabet = "абвгдеёжзийклмнопрстуфхцчщщъыьэюя"

print("Первая введенная буква находится на {} месте алфавита".format(alphabet.index(a)+1))
print("Вторая введенная буква находится на {} месте алфавита".format(alphabet.index(b)+1))
print("Между введенными буквами находится {} букв".format((alphabet.index(b)-alphabet.index(a))))
