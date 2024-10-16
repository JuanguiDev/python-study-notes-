# Operators

# Arithmetic Operators
print(3 + 2)    # Addition (+)
print(3 - 2)    # Subtraction
print(3 * 2)    # Multiplication
print(3 / 2)    # Division
print(3 % 2)    # Modulus
print(3 ** 2)   # Exponentiation
print(3 // 2)   # Floor division

# Comparison Operators
print(3 == 2)   # Equal
print(3 != 2)   # Not equal
print(3 > 2)    # Greater than
print(3 < 2)    # Less than
print(3 >= 2)   # Greater than or equal to
print(3 <= 2)   # Less than or equal to

# Logical Operators
print(3 > 2 and 4 > 3)  # AND
print(3 > 2 or 4 > 3)   # Or
print(not 3 > 2)        # Not

# Exercises

'''
    1. Write a script that prompts the user
    to enter base and height of the triangle
    and calculate an areae of this triangle
'''

b = float(input("Digite la base: "))
h = float(input("Digite la altura: "))
area = (0.5 * (b * h))
print(f"El area del triangulo es {area}")