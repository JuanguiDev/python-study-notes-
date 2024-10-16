# Variables

first_name = 'Juan'
last_name = 'Lopera'
country = 'Colombia'
city = 'Medellin'
age = 21
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Juan',
    'lastname':'Lopera',
    'country': 'Colombia',
    'city':'Medellin'
}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age);
print('Married:', is_married)
print('Skills:', skills)
print('Person Information:', person_info)

# Declaring multiple variable in a line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Inputs
name = input('What is your name?: ')
age = input('How old are you?: ')