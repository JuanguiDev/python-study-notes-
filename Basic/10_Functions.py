# Functions

# Function whithout parameters
'''
    Function can be declared without parameters.
'''

def generate_full_name():
    first_name = 'Juan'
    last_name = 'Lopera'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name()

# Function returning a value - part 1
def generate_full_name_2():
    first_name = 'Juan'
    last_name = 'Lopera'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name_2())

# Function with parameters

# Single parameter
def greetings (name):
    message = name + ', welcome to Python for everyone!'
    return message

print(greetings('Juan'))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area

print(f'El area del circulo es {area_of_circle(5)}')

# Two parameter
def full_name (first_name,last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(full_name('Juan','Lopera'))

def sum_two_numbers (num_one,num_two):
    sum = num_one + num_two
    return sum

print(f'Sum of two numbers: {sum_two_numbers(5,8)}')

# Passing arguments with key and value
'''
    If we pass the arguments with key and value, the order of the arguments does not matter.
'''
def print_fullname(first_name, lastname):
    space = ' '
    full_name = first_name + space + lastname
    print(full_name)

print_fullname(lastname = 'lopera', first_name = 'Juan')

# Function returning a value - part 2

# Returning a string: Example:
def print_name(firstname):
    return firstname
    
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name

print_full_name(firstname='Asabeneh', lastname='Yetayeh')

# Returning a number:

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2024, 2002))

# Returning a boolean
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

# Returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# Function with default parameters
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2024):
    age = current_year - birth_year
    return age;
print('Age:', calculate_age(2002))


# Arbitrary number of arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10