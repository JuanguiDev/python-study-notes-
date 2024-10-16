# Lists
'''
    A list is collection of different data types which is ordered and modifiable(mutable).
    A list can be empty or it may have different data type items.
'''

# How to create a list
lst = list()
lst = []

fruits = ['banana', 'orange', 'mango', 'lemon']                         # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']         # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']                 # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']    # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print(f"Fruits: {fruits} - Total: {len(fruits)}")
print(f"Vegetables: {vegetables} - Total: {len(vegetables)}")
print(f"Animal products: {animal_products} - Total: {len(animal_products)}")
print(f"Web techs: {web_techs} - Total: {len(web_techs)}")
print(f"Countries: {countries} - Total: {len(countries)}")

# Lists can have items of different data types
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

# Accesing list items using position indexing
print(fruits[0])
# Last index
print(fruits[(len(fruits)-1)])

# Slicing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']     # list of fruits
all_fruits = fruits[0:4]                            # it returns all the fruits
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits [1:]
print(orange_and_mango)

# Modifying Lists
fruits = ['banana','orange','mango','lemon']
fruits[0] = 'avocado'
print(fruits)
last_index = len(fruits)-1
fruits[last_index] = 'lime'
print(fruits)

# Checking items in a list
fruits = ['banana','orange','mango','lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

# Adding items
'''
    To add item to the end of an existing list we
    use the method append().
'''
# Syntax
lst = list()
lst.append('item')

fruits = ['banana','orange','mango','lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

# Inserting item into a list
'''
    Use the insert() method to insert a single item at a 
    specified index in a list
'''

# Syntax
# lst = ['item1', 'item2']
# lst.insert(index,item)
fruits = ['banana','orange','mango','lemon']
fruits.insert(2,'apple')
print(fruits)

# Removing items
fruits = ['banana','orange','mango','lemon']
fruits.remove('banana')
print(fruits)

# Removing items using pop
'''
    The pop() method removes the specified indes
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()        # Delete the las item
print(fruits)
fruits.pop(0)
print(fruits)       # ['orange', 'mango']

# Removing items using del

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)

# Clearing list items
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
fruits.clear()
print(fruits)

# Copying a list
fruits = ['banana','orange','mango','lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining
positive_numbers = [1,2,3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# Joining using extend()
num1 = [0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print(f"Numbers: {num1}")

# Counting items in a list
fruits = ['banana','orange','mango','lemon']
print(fruits.count('banana'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# Finding index of an item
fruits = ['banana','orange','mango','lemon']
print(fruits.index('banana'))   #1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence

# Reversing a list
# The reverse() method reverses the order of a list
fruits = ['banana','orange','mango','lemon']
fruits.reverse()
print(fruits)

# Sorting list items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)   # sorted in alphabetical order

fruits.sort(reverse=True)
print(fruits)