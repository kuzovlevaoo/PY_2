class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name_ = name
        self.author_ = author

    @property
    def name(self):
        return self.name_

    @property
    def author(self):
        return self.author_

    def __str__(self):
        return f'Книга: {self.name}. Автор: {self.author}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r})'


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages_ = pages

    @property
    def pages(self):
        return self.pages_

    @pages.setter
    def pages(self, val: int):
        if isinstance(val, int):
            if val <= 0:
                raise ValueError(f'Ошибка при передачи страниц')
        else:
            raise TypeError(f'Ошибка при передачи типа страниц')

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration_ = duration

    @property
    def duration(self):
        return self.duration_

    @duration.setter
    def duration(self, val: float):
        if isinstance(val, float):
            if val <= 0:
                raise ValueError(f'Ошибка в длительности записи')
        else:
            raise TypeError(f'Ошибка типа длительности записи')

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})'



