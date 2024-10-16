# Loops

# While loop
'''
    Syntax

    while condition:
        code goes here
'''

count = 0
while count < 5:
    print(count)
    count = count + 1

# Break and continue

# Break
'''
    Syntax

    while condition:
        code goes here
        if another_condition:
            break
'''

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# Continue
'''
    Syntax

    while condition:
        code goes here
        if another_condition:
            continue
'''
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1


# For loop

# For loop with list
'''
    Syntax

    for iterator in lst:
        code goes here
'''

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)


# For loop with string
'''
    Syntax

    for iterator in string:
        code goes here
'''
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])


# For loope with tuple
'''
    Syntax

    for iterator in tpl:
        code goes here
'''

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# For loop with dictionary
'''
    Syntax

    for iterator in tpl:
        code goes here

'''
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out


# Loop in set
'''
    Syntax

    for iterator in st:
        code goes here
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


# Break and continue

#Short reminder
'''
    Syntax

    for iterator in sequence:
    code goes here
    if condition:
        break
'''

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# Continue
'''
    Syntax
    for iterator in sequence:
        code goes here
        if condition:
            continue
'''

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')



# The range function
'''
    The range() function is used list of numbers.
    The range(start, end, step) takes three parameters: starting, ending and increment.
    By default it starts from 0 and the increment is 1.
    The range sequence needs at least 1 argument (end).
'''

lst = list(range(11))
print(lst)
st = set(range(1,11))
print(st)

# syntax
'for iterator in range(start, end, step):'

for number in range(11):
    print(number)


# Nested for loop
'''
    Syntax
    for x in y:
        for t in x:
            print(t)
'''

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# For else

#If we want to execute some message when the loop ends, we use else.

'''
    Syntax

    for iterator in range(start, end, step):
        do something
    else:
        print('The loop ended')
'''

for number in range(11):
    print(number)
else:
    print(f'The loop stops at {number}')


# Pass
for number in range(6):
    pass


