# Tuples
'''
    A tuple is a collection of different data types which is ordered and unchangeable (immutable).
    Tuples are written with round brackets, ().
    Once a tuple is created, we cannot change its values.
'''

# Syntax
empty_tuple = ()
empty_tuple = tuple()

# Tuple with initial values
fruits = ('banana','orange','mango','lemon')

# Tuple length
tpl = ('item1', 'item2', 'item3')
print(len(tpl))

# Accesing tuple items
fruits = ('banana','orange','mango','lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits)-1
last_fruit = fruits[last_index]

# Silicing tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

# Changing tuples to lists
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)

# Checking an item in a tuple
fruits = ('banana','orange','mango','lemon')
print('orange' in fruits)
print('apple' in fruits)

# Joining tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

# Deleting tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits