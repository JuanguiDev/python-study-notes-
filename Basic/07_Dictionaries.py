# Dictionaries

# Creating a dictionary

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Example
person = {
    'first_name':'Juan',
    'last_name':'Lopera',
    'age':'21',
    'country':'Colombia',
    'is_married':True,
    'skills': ['JS','Python','PHP','Java'],
    'addres':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# Dictionary length
'''
   It checks the number of 'key: value' pairs in the dictionary. 
'''
print(len(person)) #7

# Accessing dictionary items
print(person['first_name'])
print(person['country'])
print(person['skills'])
print(person['skills'][0])
print(person['addres']['street'])

print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

# Adding items to a dictionary
person['job_title'] = 'Software Developer'
person['skills'].append('HTML')
print(person)

# Modifying items in a dictionary
person['first_name'] = 'Juangui'
person['age'] = 22
print(person)

# Checking keys in a dictionary
print('last_name' in person)
print('city' in person)

# Removing key and value pairs from a dictionary
'''
    - pop(key): removes the item with the specified key name:
    - popitem(): removes the last item
    - del: removes an item with specified key name

'''
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item
print(person)

# Changing dictionary to a list of items
print(person.items())

# Clearing a dictionary
print(person.clear())

# Deleting a dictionary
del person

# Copy a dictionary

person = {
    'first_name':'Juan',
    'last_name':'Lopera',
    'age':'21',
    'country':'Colombia',
    'is_married':True,
    'skills': ['JS','Python','PHP','Java'],
    'addres':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

dct_copy = person.copy()
print(dct_copy)

# Getting dictionary keys as a list
keys = person.keys()
print(keys)