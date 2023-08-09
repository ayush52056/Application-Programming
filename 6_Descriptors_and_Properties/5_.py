# Before
class Person:
    def __init__(self, name):
        self.name = name

p = Person("John")

#After
class LengthValidator:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if len(value) < self.min_length:
            raise ValueError(f"{self.name} must be at least {self.min_length} characters long")
        setattr(instance, self.name, value)

class Person:
    name = LengthValidator(3)

    def __init__(self, name):
        self.name = name

p = Person("John")  # Raises ValueError: name must be at least 3 characters long
