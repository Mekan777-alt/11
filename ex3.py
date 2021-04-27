"""
Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""

from re import compile


class NumberValidationError(Exception):
    """Самопальное исключение"""

    def __init__(self, number):
        self.txt = f"NumberValidationError: {number} не является числом!"


numbers = []
REG = compile(r"^[+-]?[0-9]+\.?[0-9]*$")  #
while True:
    x = input('Введите число для добавления в список, или "end" для завершения: ')
    if x.lower() == 'end':
        print("Завершение ввода")
        break
    try:
        if not REG.match(x):
            raise NumberValidationError(x)
        numbers.append(float(x))
    except NumberValidationError as err:
        print(err.txt)
print(numbers)