#main file
from Phone import  Phone11
#object of a class = Phone11 class with data type actual of a Noun
Phone1 = Phone11("Samsung", "Business", 4.7, True)#I'm receiving from the other file containing the function
Phone2 = Phone11("XIAOMI", "Special", 4.9, True)#- calling init FUNCTION in the other file phone.py

print(Phone1.name)
print(Phone2.name)

'''
NOTES: 
OBJECT: is just one instance of a class
CLASS: It's Overall template it defines what a phone is, put an object is an actual phone with actual information
'''