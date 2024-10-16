## Classes ##

# Creating a class
'''
    Syntax
    class ClassName:
        code goes here
'''

class Person:
    pass
print(Person) # <class '__main__.Person'>

# Creating an Object
p = Person()
print(p)

# Class Constructor
class Person:
    def __init__(self,name):
        self.name = name

p = Person('Juan')
print(p.name)
print(p)

'''
    Output
    
    Juan
    <__main__.Person object at 0x00000242AD269B20>
'''
# Let us add more parameters to the constructor function.

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Juan','Lopera',21,'Colombia','Medellin')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

'''
    Output

    Juan
    Lopera
    21
    Colombia
    Medellín
'''

# Object Methods
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'
    
p = Person('Juan','Lopera',21,'Colombia','Medellin')
print(p.person_info())

'''
    Output

    Juan Lopera is 21 years old. He lives in Medellin, Colombia 
'''

# Object default methods

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

'''
    Output

    Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
    John Doe is 30 years old. He lives in Noman city, Nomanland.
'''

# Method to modify class default values

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# Inheration
'''
    Using inheritance we can reuse parent class code.
    Inheritance allows us to define a class that inherits all the methods and properties from parent class. The parent class or super or base class is the class which gives all the methods and properties.
    Child class is the class that inherits from another or parent class. Let us create a student class by inheriting from person class.
'''

class Student(Person):
    pass

s1 = Student('Juan','Lopera',21,'Colombia','Medellín')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

