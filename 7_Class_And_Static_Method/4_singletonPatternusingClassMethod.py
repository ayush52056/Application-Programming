class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True
