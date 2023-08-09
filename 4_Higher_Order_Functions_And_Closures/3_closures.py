def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_example = outer_function(10)
result = closure_example(5)
print(result)  # Output: 15
