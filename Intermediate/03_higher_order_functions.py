# Higher Order Functions

''' Function as a parameter'''
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f,lst):
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers,[i for i in range(1,6)])
print(result)   # 15


''' Functions as a Return Value '''
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))    # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3


''' Python Closures '''

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))    # 15
print(closure_result(10))   # 20


''' Built-in Higher Order Functions '''

# map
# The map() function is a built-in function that takes a function and iterable as parameters.

# Example
numbers = [i for i in range(1,6)]
def square(x):
    return x ** 2
numbers_squared = map(square,numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

numbers_squared = map(lambda x: x ** 2,numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# filter
# The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). 

numbers = [i for i in range(1,6)]
def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even,numbers)
print(list(even_numbers))   # [2, 4]


# Reduce
'''
    The reduce() function is defined in the functools module and we should import it from this module.
    Like map and filter it takes two parameters, a function and an iterable.
    However, it does not return another iterable, instead it returns a single value.
'''

# Example
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15