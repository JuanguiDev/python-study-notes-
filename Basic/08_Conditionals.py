# Conditionals

# If Condition
'''
    Syntax

    if condition:
        this part of code runs for truthy conditions
'''

a = 3
if a > 0:
    print('A is a positive number')


# If Else
'''
    Syntax

    if condition:
        this part of code runs for truthy conditions
    else:
        this part of code runs for false conditions
'''

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')


# If Elif Else
'''
    Syntax

    if condition:
        code
    elif condition:
        code
    else:
        code
'''

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is a zero')


# Short hand
'''
    Syntax

    code if condition else code
'''

a = 3
print('A is a positive number') if a > 0 else ('A is negative')


# Nested conditions
'''
    Syntax

    if condition:
        code
        if condition:
        code
'''

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


# If condition and logical operators
'''
    Syntax

    if condition and condition:
        code
'''

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or logical operators
'''
    Syntax

    if condition or condition:
        code
'''

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')