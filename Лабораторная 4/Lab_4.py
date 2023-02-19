if __name__ == "__main__":

    class Person:
        """Base class for persons"""

        def __init__(self, name: str, age: int, gender: str):
            self.name = name
            self.age = age
            self.gender = gender

        def existing(self) -> bool:
            """Function that checks the existence of the person"""

        def __str__(self):
            return f"Cat({self.name}, {self.age}, {self.gender})"

        def __repr__(self):
            return f"Cat({self.name!r}, {self.age!r}, {self.gender!r})"


    class Employee(Person):
        """Class for employees"""

        def __init__(self, name: str, age: int , gender: str, work: str):
            super().__init__(name, age, gender)
            self.work = work

        @property
        def work(self) -> str:
            return self.work
        """This methods is to indicate work program"""

        @work.setter
        def work(self, value: str) -> None:
            if not isinstance(value, str):
                raise ValueError('Text only allowed')
            if value:
                raise ValueError('Enter text')

        def __str__(self):
            return f"Employee({self.name}, {self.age}, {self.gender}, {self.work})"

        def __repr__(self):
            return f"Employee({self.name!r}, {self.age!r}, {self.gender!r}, {self.work!r})"

        def existing(self) -> bool:
            """Function that checks the existence of the empolyee"""


    class Student(Person):
        """Class for students"""

        def __init__(self, name: str, age: int, gender: str, study: str):
            super().__init__(name, age, gender)
            self.study = study

        @property
        def study(self) -> str:
            return self.study
        """This methods is to indicate study program"""

        @study.setter
        def study(self, value: str) -> None:
            if not isinstance(value, str):
                raise ValueError('Text only allowed')
            if value:
                raise ValueError('Enter text')

        def __str__(self):
            return f"Student({self.name}, {self.age}, {self.gender}, {self.study})"

        def __repr__(self):
            return f"Student({self.name!r}, {self.age!r}, {self.gender!r}, {self.study!r})"

        def existing(self) -> bool:
            """Function that checks the existence of the student"""


