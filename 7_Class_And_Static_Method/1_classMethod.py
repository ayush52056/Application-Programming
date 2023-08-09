class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

obj1 = MyClass()
obj2 = MyClass()

print(obj1.get_count())  # Output: 2
print(obj2.get_count())  # Output: 2
