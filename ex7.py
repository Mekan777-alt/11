"""
Реализовать проект «Операции с комплексными числами».
    Создать класс «Комплексное число».
    Реализовать перегрузку методов сложения и умножения комплексных чисел.
    Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
"""
from re import compile


class NumberValidationError(Exception):
    """Самопальное исключение"""

    def __init__(self, number):
        self.txt = f"NumberValidationError: {number} не является числом!"


class ComplexNumber:
    """Самодельное комплексное число"""

    def __init__(self, a, b=0.0):
        """Инициация, под распакованные списки с лишними элементами"""
        self.a = str_to_num(a)
        self.b = str_to_num(b)

    def __add__(self, other):
        """Перегруз сложения, принимает как комплексные так и вещественные числа"""
        if type(other) == int or type(other) == float:
            return ComplexNumber(round(self.a + other + 5 / 10 ** 8, 2), self.b)
        else:
            return ComplexNumber(round(self.a + other.a + 5 / 10 ** 8, 2),
                                 round(self.b + other.b + 5 / 10 ** 8, 2))

    def __mul__(self, other):
        """Перегруз сложения, принимает как комплексные так и вещественные числа"""
        if type(other) == int or type(other) == float:
            return ComplexNumber(round(self.a * other + 5 / 10 ** 8, 2),
                                 round(self.b * other + 5 / 10 ** 8, 2))
        else:
            return ComplexNumber(round(self.a * other.a - self.b * other.b + 5 / 10 ** 8, 2),
                                 round(self.a * other.b + self.b * other.a + 5 / 10 ** 8, 2))

    def __str__(self):
        """Перегруз преобразования в строку"""
        return f"{self.a}" \
               f"{' - ' if self.b < 0 else ' + ' if self.b != 0 else ''}" \
               f"{str(abs(self.b)) + 'i' if self.b != 0 else ''}"


def str_to_num(num):
    """Проверка строк на валидность с возвратом числа"""
    if type(num) == float:
        return num
    reg = compile(r"^[+-]?[0-9]+\.?[0-9]*$")
    if not reg.match(num):
        raise NumberValidationError(num)
    return float(num)


def compl_():
    """Функция запроса комплексного числа"""
    numbs = []
    while len(numbs) < 1:
        numbs = input('Введите a и b (вещественную и мнимую величины) через пробел: ').split()
    return ComplexNumber()


def numb():
    """Функция запроса вещественного числа"""
    return str_to_num(input('Введите число: '))


type_dict = {'1': compl_, '2': numb}
while True:
    nums = input('Введите a и b (вещественную и мнимую величины) через пробел, или не вводите для завершения: ')
    if not nums:
        print('\nЗавершение программы...')
        break
    try:
        number_1 = ComplexNumber()
        type_ = input('Введите 1 для создания комплексного числа или иное для вещественного: ')
        number_2 = type_dict.get(type_, numb)()
        print('Полученные числа:', number_1, number_2, sep='\n')
        print(f'\n({number_1}) + ({number_2}) = {number_1 + number_2}')
        print(f'({number_1}) x ({number_2}) = {number_1 * number_2}\n\n')
    except NumberValidationError as err:
        print(err.txt)
        print('Попробуйте ещё, введя правильные данные!')