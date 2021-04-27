"""
Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных
"""


class DateValidationError(Exception):
    """Ошибка корректности даты"""

    def __init__(self, value):
        self.txt = f'DateValidationError: [{value}] не является корректной датой'


class MyDate:
    """Самодельный формат даты"""
    splitters = {'/', ',', '.', '-', ' '}

    def __init__(self, date_string: str):
        """Конструктор даты, преобразовывает строку в самодельный формат даты"""
        raw_date = self.str_conv(date_string)
        validate_date = self.date_validation(raw_date)
        if validate_date:
            self.date = {'day': raw_date[0], 'month': raw_date[1], 'year': raw_date[2]}
        else:
            raise DateValidationError(date_string)

    def __str__(self):
        """Перегрузка строки приведением формата даты"""
        return f'{self.date["day"]:02}.{self.date["month"]:02}.{self.date["year"]:02}г.'

    @classmethod
    def str_conv(cls, date_string: str):
        """Разбивает строку по валидным разделителям и преобразовывает подстроки в числа"""
        date_list = []
        for spl in cls.splitters:
            if spl in date_string:
                date_list = date_string.split(spl)
                break
        if not date_list:
            raise DateValidationError(date_string)
        for i, number in enumerate(date_list):
            if number.isdigit():
                date_list[i] = int(date_list[i])
            else:
                raise DateValidationError(date_string)
        return tuple(date_list)

    @staticmethod
    def date_validation(r_date: tuple):
        """Валидация сырой даты перед преобразованием"""
        fer_days = 28 if r_date[2] % 4 else 29
        days_dict = {1: 31, 2: fer_days, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if len(r_date) == 3 and 0 < r_date[0] <= days_dict.get(r_date[1], 0):
            return True
        return False


while True:
    date_str = input("Введите дату в формате дд мм гггг\n"
                     f"Возможные разделители: {MyDate.splitters}\n"
                     "Для завершения ничего не вводите, нажмите [Enter]\n>>> ")
    if not date_str:
        print('\nЗавершение работы.')
        break
    try:
        date_date = MyDate(date_str)
    except DateValidationError as err:
        print(f'\n{err.txt}\n')
    else:
        print(f'\nДата получена успешно: {date_date}\n')