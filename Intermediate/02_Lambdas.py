# Lambda

'''Lambda function is a small anonymous function without a name'''

# Example
# Named Function
def add_two_nums(a,b):
    return a + b

print(add_two_nums(5,4))    # 9
# Lets change the above function to a lambda function
add_two_nums = lambda a,b: a + b
print(add_two_nums(5,4))    # 9

square = lambda x: x ** 2
print(square(5))    # 25
cube = lambda x: x ** 3
print(cube(3))      # 27


''' Lambda Function Inside Another Function '''
# Using a lambda function inside another function

def power(x):
    return lambda n: x ** n
cube = power(3)(3)
print(cube)         # 27
