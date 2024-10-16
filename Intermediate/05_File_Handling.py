# File Handling

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermediate/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Juan\nMi apellido es Lopera\n22 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Java")
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")
# .json file


json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Juan",
    "surname": "Lopera",
    "age": 22,
    "languages": ["Python", "Swift", "Kotlin"]}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language"])
csv_writer.writerow(["Juan", "Lopera", 22, "Python"])
csv_writer.writerow(["Roswell", "", 2, "COBOL"])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file