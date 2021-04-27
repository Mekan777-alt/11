"""
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

from re import compile


class MyZeroDivizion(Exception):
    """Самопальное исключение зиро дивижен"""
    txt = "MyZeroDivizion: деление на ноль!"


REG = compile(r"^[+-]?[0-9]+\.?[0-9]*$")
while True:
    x = input('Введите делимое: ')
    y = input('Введите делитель: ')
    if not REG.match(x) or not REG.match(y):
        print('Требуется ввести числа!', '\n')
        continue
    x = float(x)
    y = float(y)
    try:
        if not y:
            raise MyZeroDivizion
        print(round(x / y + 5 / 10 ** 8, 2), '\n')
    except MyZeroDivizion as err:
        print(err.txt, '\n')
    more = input('Введите "да", если хотите повторить: ')
    if more.lower() != 'да':
        print('Завершение программы')
        break