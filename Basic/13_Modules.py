# Importing a module
import mymodule
print(mymodule.generate_full_name('Juan','Lopera')) # Juan Lopera

# Import Functions from a module
from mymodule import generate_full_name,sum_two_nums
print(generate_full_name('Juan','Lopera'))  # Juan Lopera
print(sum_two_nums(1,5))    #6

# Import functions from a module and renaming
from mymodule import generate_full_name as full_name, sum_two_nums as total
print(full_name('Juan','Lopera'))   # Juan Lopera
print(total(1,9))   # 10

# Statistics module
from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # 21.9
print(median(ages))     # 22
print(mode(ages))       # 20
print(stdev(ages))      # 6.106

# Math Module
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

from math import pi
print(pi)

# It is also possible to import multiple functions at once
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

# But if we want to import all the function in math module we can use * .
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

# When we import we can also rename the name of the function.
from math import pi as  PI
print(PI) # 3.141592653589793

# Randome module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive