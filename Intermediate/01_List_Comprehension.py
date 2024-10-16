# List Comprehension

# One way
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

# Second way: list comprehension
lst = [i for i in language]
print(type(lst))
print(lst)

# Generating numbers
numbers = [i for i in range(11)]    # to generate numbers from 0 to 10
print(numbers)                      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It's possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                      # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


''' List comprehension can be combined with if expression '''
# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)                 # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)                  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)
