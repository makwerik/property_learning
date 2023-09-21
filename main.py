"""
Практика с методом property, путём создания класса человека с именем, возрастом и последующим изменением его возраста
"""

class Person:
    def __init__(self, name, old):
        """
        Устанавливаем protect атрибуты класса
        """
        self.__name = name
        self.__old = old

    @property
    def old(self):
        """
        Метод (являющийся геттером), обернутый в декотратор property возвращающий возраст человека
        """
        return self.__old

    @old.setter
    def old(self, old):
        """
        Метод (явяющийся сеттером), обернутый так же в декоратор property от сеттора. Изменяет значение атрибута
        """
        self.__old = old

    @old.deleter
    def old(self):
        """
        Метод (являющийся делитером), для удаления свойства old
        """
        del self.__old


if __name__ == "__main__":
    people = Person('Маквэрик', 23)
    print(people.old)
    hb = people.old = 24
    print('После 07.10.2023 мне уже будет:' + str(hb))

