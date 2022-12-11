import doctest

class Empoloyee:
    '''
    Создание и подготовка к работе объекта 'Работник'
    :param name: Имя работника
    :param work_hours: Количество рабочих часов
    :param salary: Заработная плата
    Примеры:
    >>> employee = Empoloyee('Влад', 30, 40000)  # инициализация экземпляра класса
    '''
    def __init__(self, name: str, work_hours: int, salary: int):
        self.name = name
        self.work_hours = work_hours
        self.salary = salary


    def increase_work_hours(self, add_work_hours: int) -> int:
        '''
        Функция, которая увеличивает количество рабочих часов
        :param add_work_hours: добавсленное количество рабочих часов
        :return: новое количество рабочих часов
        Примеры:
        >>> employee = Empoloyee('Влад', 30, 40000)
        >>> employee.increase_work_hours(1)
        '''
        if not isinstance(add_work_hours, int):  #проверяем тип данных
            raise TypeError  #вызываем ошибку, если тип данных не int
        if add_work_hours > 40: #считаем, что законы работают, поэтому в месяц максимум 40 часов работы
            raise ValueError



    def icreased_salary(self, add_salary: int) -> int:
        '''
        Функция, которая увеличивает заработную плату
        :param add_salary: добавсленная заработная плата
        :return: новая заработная плата
        Примеры:
        >>> employee = Empoloyee('Влад', 30, 40000)
        >>> employee.icreased_salary(10000)
         '''
        if not isinstance(add_salary, int):  #проверяем тип данных
            raise TypeError  #вызываем ошибку, если тип данных не int



if __name__ == '__main__':
    doctest.testmod()


class Plate:
    def __init__(self, volume: int, food_volume: int):
        '''
        Создание и подготовка к работе объекта 'Тарелка'
        :param volume: Объем тарелки
        :param food_volume: Объем, который занимает еда
        Примеры:
        >>> plate = Plate(500, 0)  # инициализация экземпляра класса
        '''
        if not isinstance(volume, int):
            raise TypeError('Объем тарелки должен быть типа int')
        if volume <= 0:
            raise ValueError('Объем тарелки должен быть положительным числом')
        self.volume = volume

        if not isinstance(food_volume, int):
            raise TypeError('Количество еды должно быть int')
        if food_volume < 0:
            raise ValueError('Количество еды не может быть отрицательным числом')
        self.food_volume = food_volume

    def empty_plate(self) -> bool:
        '''
        Функция которая проверяет является ли тарелка пустой
        :return: Является ли тарелка пустой
        Примеры:
        >>> plate = Plate(500, 0)
        >>> plate.empty_plate()
        '''

    def add_food_to_plate(self, food: int) -> None:
        '''
        Добавление еды в тарелку.
        :param food: Объем добавляемой еды
        :raise ValueError: Если количество добавляемой еды превышает свободное место в тарелке, то вызываем ошибку
        Примеры:
        >>> plate = Plate(500, 0)
        >>> plate.add_food_to_plate(200)
        '''
        if not isinstance(food, int):
            raise TypeError('Добавляемая еда должна быть типа int')
        if food < 0:
            raise ValueError('Добавляемая еда должна положительным числом')
        ...

    def remove_food_from_plate(self, estimate_food: int) -> None:
        '''
        Извлечение eды из тарелки.
        :param estimate_food: Объем извлекаемой еды
        :raise ValueError: Если количество извлекаемой еды превышает количество еды в тарелке,
        то возвращается ошибка.
        :return: Объем реально извлеченной еды
        Примеры:
        >>> plate = Plate(500, 0)
        >>> plate.remove_food_from_plate(200)
        '''



if __name__ == '__main__':
    doctest.testmod()

class Man:
    def __init__(self, name: str, age: int, gender: str):
        '''
        Создание и подготовка к работе объекта 'Человек'
        :param name: Имя человека
        :param age: Возраст человека
        :param gender: Пол человека
        Примеры:
        >>> man = Man('Алексей', 23, 'male')  # инициализация экземпляра класса
        '''

        if not isinstance(name, str):
            raise TypeError('Имя человека должно быть типа str')
        if len(name) <= 0:
            raise ValueError('Имя человека должно иметь хотя бы один символ')
        self.name = name

        if not isinstance(age, int):
            raise TypeError('Возраст человека должно быть типа int')
        if age <= 0:
            raise ValueError('Возраст человека не может быть меньше либо равен 0')
        self.age = age

        if not isinstance(gender, str):
            raise TypeError('Пол человека должен быть типа str')
        self.gender = gender
        if len(gender) <= 0:
            raise ValueError('Пол человека должен иметь хотя бы один символ')
        self.gender = gender


    def existing(self) -> bool:
        '''
        Функция которая проверяет существует ли человек
        :return: Является ли человек существующим
        Примеры:
        >>> man = Man('Алексей', 23, 'male')
        >>> man.existing()
        '''

    def growing(self, add_age: int) -> int:
        '''
        Взросление человека.
        :param add_age: Количество добавленных лет
        :raise ValueError: Если количество добавляемых лет меньше либо равно 0, то вызываем ошибку
        Примеры:
        >>> man = Man('Алексей', 23, 'male')
        >>> man.growing(2)
        '''

if __name__ == '__main__':
    doctest.testmod()
