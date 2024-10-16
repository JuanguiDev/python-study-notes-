# Sets
'''
    Set is a collection of unordered and un-indexed distinct elements.
'''

# Creatin sets
# Syntax
st = set()
st = {'item1','item2','item3'}

fruits = {'banana','orange','mango','lemon'}

# Getting sets length
fruits = {'banana','orange','mango','lemon'}
len(fruits)

# Checking an item
fruits = {'banana','orange','mango','lemon'}
print('mango' in fruits)

# Adding items to a set
'''
    Once a set is created we can not change any items and
    we can also add additional items
'''

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

'''
    We can add multiple items using update()
'''

fruits = {'banana','orange','mango','lemon'}
vegetables = ('tomato','potato','cabbage','onion','carrot')
fruits.update(vegetables)
print(fruits)

# Removing item from a set

ruits = {'banana','mango','orange','lemon'}
fruits.remove('mango')
print(fruits)

'''
    The pop() methods remove a random item from a list and it returns the removed item.
'''

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(fruits)

# Clearing items in a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# Deleting a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

# Joining Sets
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Update this method inserts a set into a given set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Finding intersection items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

# Checking the Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
