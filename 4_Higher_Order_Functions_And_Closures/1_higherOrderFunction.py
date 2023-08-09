def apply(func, x):
    return func(x)

def double(x):
    return x * 2

result = apply(double, 5)
print(result)  # Output: 10


def apply_function(func, n):
    return func(n)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

result = apply_function(square, 3)
print(result)  # Output: 9

result = apply_function(cube, 3)
print(result)  # Output: 27
