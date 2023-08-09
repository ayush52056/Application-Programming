def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

num1 = 10
num2 = 5

print(f"{num1} + {num2} = {add(num1, num2)}")          # Output: 10 + 5 = 15
print(f"{num1} - {num2} = {subtract(num1, num2)}")     # Output: 10 - 5 = 5
print(f"{num1} * {num2} = {multiply(num1, num2)}")     # Output: 10 * 5 = 50
print(f"{num1} / {num2} = {divide(num1, num2)}")       # Output: 10 / 5 = 2.0
