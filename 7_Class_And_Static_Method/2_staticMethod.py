class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

result1 = MathOperations.add(5, 3)
print(result1)  # Output: 8

result2 = MathOperations.multiply(5, 3)
print(result2)  # Output: 15
