# Error Types

# SyntaxError
# print 'hello world'
''' SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)? '''
print('Hello world')    # Hello world


# NameError
# print(age)
''' NameError: name 'age' is not defined '''
age = 22
print(age)


# IndexError
numbers = [i for i in range(1,6)]
# numbers[5]
''' IndexError: list index out of range '''


# ModuleNotFoundError
# import maths
''' ModuleNotFoundError: No module named 'maths' '''
import math


# AttributeError
# math.PI
''' AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?  '''
print(math.pi)


# TypeError
# print(4 + '3')
''' TypeError: unsupported operand type(s) for +: 'int' and 'str' '''
print(4 + int('3'))


# ImportError
# from math import power
''' ImportError: cannot import name 'power' from 'math' (unknown location) '''
from math import pow
print(pow(3,2))


# ValueError
# int('12a')
''' ValueError: invalid literal for int() with base 10: '12a' '''


# ZeroDivisionError
# print(1/0)
''' ZeroDivisionError: division by zero '''