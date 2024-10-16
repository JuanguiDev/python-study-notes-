# Strings

# Creating a string
greeting = "Hello, World!"
print(greeting)
print(len(greeting))

# String concatenation
first_name = 'Juan'
last_name = 'Lopera'
space = ' '
full_name = first_name + space + last_name
print(full_name)

# Escape Sequences in Strings
# %s - String
# %d - Integer
# %f - Float

print('I hope everyone is enjoying the Python Challenge. \nAre you?')   # Line break '\'
print('Days\tTopics\tExcercises')                                       # Adding tab space
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol (\\)')                                # To write a line

# String formatting
language = 'Python'
formated_string = 'I am %s %s. I am studying %s'%(first_name,last_name,language)
print(formated_string)

formated_string = 'I am {} {}. I am studying {}'.format(first_name,last_name,language)
print(formated_string)

# String Interpolation
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Unpacking Characters
a,b,c,d,e,f = language
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Slicing Python String
first_three = language[0:3]
print(first_three)          #Pyt
last_thre = language[3:6]
print(last_thre)            #Hon

# Reversing a String
print(greeting[::-1])       # dlroW ,olleH

# Skipping Characters While Slicing
pto = language [0:6:2]
print(pto)

# String Methods

challenge = 'thirty days of python'
print(challenge.capitalize())       # Capitalize(): Converts the first character of the string to capital letter
print(challenge.count('y'))         # Count the 'letter' in the word
print(challenge.upper())            # All upper letters
print(challenge.lower())            # All lower letters
