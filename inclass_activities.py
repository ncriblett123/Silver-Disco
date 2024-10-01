"""basic commands to know"""
# newline = \n
# tab = \t
# print(i, end = ' ') makes the end a space instead of a new line
"***************************************************"
# imports #
from statistics import * #imports statistics
from decimal import Decimal #imports decimal
import os
import csv



"***************************************************"

# 2/1/24 #

""" 
y = int(input('Input an integer\n'))
y = y % 2
if y%2==0:
    print('even')
else:
    print('odd')
    """  

"***************************************************"

# 2/13/24 #

#if-then
"""
x = 10
if x<20: #need a : for "then" 'x<20' - boolean expression evaluated true or false
    statment
    print("hello")
"""
#if-then-else
"""
x = 10
if x < 20:
   print("x is less than 20")
else: # again need :
    print("x is not less than 20")
    """

#if-elif-elif...else
"""
x = 10
if x < 5:
    print('x is less than 5')
elif x < 10:
    print("x is less than 10")
elif x < 20:
    print("x is less than 20")
else:
    print(x)
    """

#This breaks a 5 digit number down to the individual numbers

"""
userImput = int(input("Enter a 5 diget number\n"))
n5 = userImput % 10
userImput = userImput // 10

n4 = userImput % 10
userImput = userImput // 10

n3 = userImput % 10
userImput = userImput // 10

n2 = userImput % 10
userImput = userImput // 10

n1 = userImput % 10

print(n1,n2,n3,n4,n5)
"""

"***************************************************"

# 2/15/24 #

#Boolean operator - and, or, not
# AND - both must be true
# OR - either opperator must be true
# NOT - opperates on one opperator, flips it from true to false or vis versa


#AND
"""
y = 3
x = 5
if x < 10 and y < 5:    #true and true = TRUE
    print('success')

if x <10 and y < 5:     #true and flase = FALSE
    print('success yes')

if x < 4 and y < 3:     #flase and false = FALSE
    print('hi')
"""
    
#OR
"""
x = 5
y = 3
if x < 10 or y < 3:     #true or false = TRUE
    print('hello')

if x < 10 or y < 5:     #true or true = TRUE
    print('hello')

if x < 4 or y < 2:     #false or flase = FALSE
    print('hello')
"""
#NOT
"""
x = 5
y = 3
if not (x < 4) or y < 2:    #not flase or false = TRUE
    print('hi')

if not(x < 4 or y < 2):     #not flase = TRUE
    print('hi')
"""
#while loops
#need a pre-read, loop while boolean expression is TRUE

"""
x = 5 #pre-read
y = 3 #pre-read


while x < 10:
    print("hello")
    x = x + 1
    if x == 10:
        break
print('done')


while y < 5 and x < 7: #can use multiple opperators
    print('hi')
    x = x + 1
    """

# for loops
# range()- range function, iterable list, will iterate for the number in the range funchtion

"""
for i in range(5): #variable is initalised, boolean codition is checked, increment or decrement
    print(i)
    """

# formated print
"""
x = 32.5555555
print(f'{x}')
print(f'{x:.2f}') #f means formated print, .2f prints 2 decimals to the right and rounds up
print(f'{x:.2%}') # turns the number into a percent
print(x, end = ' ') #will print a space at the end istead of a new line
"""
#augmented allignmnet
"""
x = 123
print(f'{x:>10}') #moves x 10 spaces to the right
"""

#augmented assignment
"""
x = 0
'''increment a variable'''
x = x + 1
x += 1 
'''decrement a variable'''
x = x - 1
x -= 1
'''multiplication'''
x = x * 10
x *= 10
'''division'''
x = x / 10
x /= 10
"""

#Module 4 Assignment
"""
a = b = 7
print('a =', a, '\nb =',b)
"""
'''
number1 = int(input('Enter first integer: '))

number2 = int(input('Enter second integer: '))
x = 0

if number1 == number2:
    print(number1, 'is equal to', number2)
    print(number1, 'is less than or equal to',number2) 
    print(number1, 'is greater than or equal to', number2)
    x = 1
else:
    print(number1, 'is not equal to',number2)

if (number1 > number2):
    print(number1,'is greater than', number2)
elif number1 < number2:
    print(number1,'is less than', number2)

if (number1 >= number2) and x != 1:
    print(number1, 'is greater than or equal to', number2)
elif (number1 <= number2) and x != 1:
    print(number1, 'is less than or equal to', number2)

input('What is your problem?')

userImput = str(input("Have you had thos problem before (yes or no)?"))

if userImput == 'yes':
    print('Well, you have is again.')
elif userImput == 'no':
    print('Well, you have it now')
'''
"***************************************************"

# 2/20/24 #

# Lists or Arrays
'''
myList = [0, 1, -1, 5, 3]
'''
#indexes  0  1   2  3  4

'''
for i in myList:
    print(i)

print(myList[2])


cList=[]
cList.append('5') #adds '5' so the empty cList
cList.insert(1,3.14) #puts 3.14 at index 1

myList = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
average = count = 0

for i in myList:
    average = average + i
    count = count + 1
average = average / count
print(average)
'''
#nested for loops
'''
for i in range(5):
    for j in range(5):
        print(i,j)
'''
#in class activity
'''
i = 1
j = 5
k = 7
m = 2
print((i >= 1) and (j < 4))
print((m <= 99) and (k < m))
print((j >= i) or (k ==m))
print((k + m < j) or (3 - j >= k))
print(not(k > m))


myList = [0, 3, 6, 9, 12, 15]
average = count = 0

print(myList[0],'is the first number and', myList[5],'is the last number')


for i in myList:
    average +=  i
    count +=  1
average = average / count
print('The average of this list is', average)
'''

"***************************************************"

# 2/27/24 #

'''
for i in range(1,5): #two argument range function
    print(i)
for i in range(10,16):
    print(i)
for i in range(2,11,2): #three argumment, 2-11 in increments of 2
    print(i)

for i in range (5):     #Nested for loops, loop within a loop, loopception
    for j in range (3):
        print(i,j)

max = 10
i = 0

while i < max:
    if i == 5:
        break
    print(i)
    i = i + 1
print('done')

i = 0
max  = 5
while i < max:
    if i == 3:
        continue
    print(i)
    i += 1
'''

"***************************************************"

# 2/29/24 #

# sentinel-controlled iteration
# sentinel value tells the program to stop, a value that would never be seen

'''
total = 0
gradeCounter = 0
prompt = 'Enter a grade, -1 to end: '

grade = int(input(prompt))

while grade != -1: # -1 is the setinal value, will quit if a -1 
    total = total + grade
    gradeCounter += 1
    grade = int(input(prompt))

if gradeCounter != 0:
    average = total / gradeCounter
    print(f'Class average is {average:.2f}')
else:
    print('Not grades were entered')

'''

#in-class activitie 2.10
'''
sum = 0 
average = 0
product = 1
smallNum = 9999
largeNum = -9999

for i in range (4):
    myNum = int(input('Enter a number: '))
    sum += myNum
    product *= myNum
    if myNum < smallNum:
        smallNum = myNum
    if myNum > largeNum:
        largeNum = myNum

print(f'Sum: {sum}')
print(f'Product: {product}')
print(f'Largest: {largeNum}')
print(f'Smallest: {smallNum}')
print(f'Average: {sum / 4:.2f}')
'''
"***************************************************"

# 3/7/24 #
'Validate User Imput' 
#We want the user to imput the integer one
"""
userNum = int(input("Enter the number 1... please: "))

while userNum != 1:
    print("Error! You didn't listen. Enter the number 1")
    userNum = int(input("Enter the number 1... please: "))

print(f'Thank you for entering the number {userNum}!')

"""
#in-class activity
'''
myList = ['yes', 'no', 'Yes', 'No', 'YES', 'NO']

userVote = (input("Do you plan to vote this November? (yes or no): "))

while userVote not in myList: #checking user input against a list
    print('Error! You did not enter yes or no.\n')
    userVote = (input("Do you plan to vote this November? (yes or no): "))
print("Thank you for your response!")

while userVote != 'yes' and userVote != 'no': #checking the user varibale
    print('Error! You did not enter yes or no.\n')
    userVote = str(input("Do you plan to vote this November? (yes or no): "))

print("Thank you for your response!")
'''
#group work
'''
for i in range (2):
    for j in range (10):
        print("+", end ='')
    print()
'''

# Module 5 Assignment #
"""
passes = 0 #number of passes

for student in range (10): #Gets info for 10 students
    result = int(input("Enter result (1 = pass, 2 = fail): "))

    while result != 1 and result != 2: #loops if 1 or 2 is not entered
        print("You did not enter 1 or 2")
        result = int(input("Enter result (1 = pass, 2 = fail: )"))
    
    if result == 1: #increases passes by 1 if 1 is entered
        passes = passes + 1

print('Passes: ', passes)
print('Failed: ', 10 - passes)


for i in range(2):
    for j in range(7):
        print('@', end ='')
    print()

number = 0
square = 1
cube = 1

print('number   square   cube')

for i in range(6):
    square = number ** 2
    cube = number ** 3
    print(f'{number:> 6}{square:> 9}{cube:> 7}')
    number = number + 1
"""

"***************************************************"

# 3/12/24 #
# Functions 
'''
MYGLOBAL = 10 #Global variable

#define a function
def sayHello(myFloat, myBoolean): # myFloat is a parameter
    myInt = 5 #local variabl
    print(f'Hello {myInt} {myFloat} {myBoolean} {MYGLOBAL}')
    

#call a function with an argument
sayHello(3.14, True) #3.14 is an argument 

def Cubed(myInt):
    myInt = myInt ** 3
    return(myInt)

print()
myNum = int(input("Enter a number you would liked cubed: "))
cubedNum = Cubed(myNum)
print(f"Your number: {myNum}    cubed is: {cubedNum}\n")


def main():
    myInt1 = int(input("Enter your first integer: "))
    myInt2 = int(input("Enter your first integer: "))
    calcAverage(myInt1, myInt2)

def calcAverage(myInt1, myInt2):
    sum = myInt1 + myInt2
    average = sum / 2
    print(f'The average of {myInt1} and {myInt2} is {average}')

main()
'''
"***************************************************"

# Module 6 Assignment #
#4.5


'''
def seconds_since_midnight(time):
    hour_in_seconds = (time // 10000) * (3600)
    minute_in_seconds = ((time % 10000) // 100) * 60
    return(hour_in_seconds + minute_in_seconds + time % 100)

userNum = int(input("Enter a time: "))
print(seconds_since_midnight(userNum))

def main():
    uderNum = int(input("Enter a time: "))
    print(seconds_since_midnight(uderNum))
    '''
"***************************************************"
# 4/23/24
#Strings

'''
print(f'{17.489:.2f}') #rounds a float to the 2nd decimal
print(f'{10:d}') #creates a decimal
print(f'{10:b}') #outputs in binary
print(f'{10:o}') #Prints out octal, octal is base 8 numbering system
print(f'{10:X}') #Prints out in hexidecimal, base 16 0-9 then A-F: 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
print(f'{65:c} {97:c}') #Prints the ASCII character
print(f'{Decimal("1000000000000000000000.0"):.3E}') #prints scientific notation
print(f'[{17:10d}]') #Prints 10 spaces before 17
print(f'[{3.5:10f}]')
print(f'[{27:<15f}]') #Prints left allign
print(f'[{3.5:>15.2f}]') #Prints right allign
print(f'[{27:+010d}]') #Prints 0 infront of 27
print(f'{1234567:,d}') #Seperates the numbers by commas
print('{:*>12.2f}'.format(11.256))


#Class actvities
print(f'{58:c}{94:c}{41:c}')
print('{:c}{:c}{:c}'.format(58,94,41))


fName = 'Nick'
lName = ' Riblett'
fullName = fName + lName
astricks = '*'
astricks *= len(fullName)
print(f"{astricks}\n{fullName}\n{astricks}")
#.title() capitalizes the first letter of every word
#.capitalize() capitalizes the first letter of the first word
'''
"***************************************************"
# 4/30/24 #
#Reading and Writing to and from files
'''
with open('accounts.txt', mode = "w") as accounts #Opens account.txt. 'accounts' is how we refer to it later
    accounts.write('100 Jones 24.98\n)
'with' opens the file and closes it after you're done writing
'r'-Open a text file for reading
'w' -Open a text file for writing
'a'-open a text file for appending at the end
'r+' -open a text file for reading and writing
'w+' -open a text file for reading and writing. Exsisting file contents are deleted
'a+' -open a tex file for reading and writing and appending at the end
in python window, after file is created, 'dir' will show files, 'more 'fileName' will show what's in the file
'dir a*' will show all files that start with a
'filename'.readline # reads the first line of the file
'filename'.read #Will read the whole file
aFile = open('fileName.txt', mode = w)
aFile.close
fileName.seak(#) will starting reading and writing from that position
'''

#Writing to a file
'''
with open('accounts.txt', mode = 'w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 White 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')

#Reading a file

with open('accounts.txt', mode = 'r') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balence":>10}')
    for records in accounts:
        account, name, balence = records.split()
        print(f"{account:<10}{name:<10}{balence:>10}")
'''
#Updating a file
#open accounts.txt as read only
#open a temp.txt file as write only
#Write each line for account.txt to the temp.txt file
#delete OG file
#Rename temp file
'''
accounts = open('accounts.txt', 'r')
temp_file = open('temp_file.txt', 'w')
with accounts, temp_file:
    for record in accounts:
        account, name, balence = record.split()
        if account != '300':
            temp_file.write(record)
        else:
            new_record = ' '.join([account, 'Williams', balence])
            temp_file.write(new_record + '\n')
import os    
os.remove('accounts.txt') #deletes accounts.txt
os.rename('temp_file.txt', 'accounts.txt') #renames temp file to accounts.txt
'''
"***************************************************"
# 5/2/24 #
#CSV Files, comma seperated values
import csv
'''
with open('accounts.csv', mode='w', newline='') as accounts:
	writer = csv.writer(accounts)  # returns an object that writes CSV data to the specified file object
	writer.writerow([100, 'Jones', 24.98]) # writerow method receives an iterable and delimits values with commas
	writer.writerow([200, 'Doe', 345.67])
	writer.writerow([300, 'White', 0.00])
	writer.writerow([400, 'Stone', -42.16])
	writer.writerow([500, 'Rich', 224.62])
	
with open('accounts.csv', 'r', newline='') as accounts:
	print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
	reader = csv.reader(accounts)
	for record in reader:
		account, name, balance = record
		print(f'{account:<10}{name:<10}{balance:>10}')
'''

#Exceptions
#Handling exceptions
'''
while True:
    try:
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter denominator: '))
        result = number1 / number2
    except ValueError: # tried to convert non-numeric value
        print('You must enter two integers\n')
    except ZeroDivisionError:  # denominator was 0
        print('Attempted to divide by zero\n')
    else:  # executes only if no exceptions occur
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
        break # terminate the loop

def try_it(value):
    try:
       x = int(value)
    except ValueError:
       print(f'{value} could not be converted to an integer')
    else:
       print(f'int({value}) is {int(value)}')
    finally:
       print('finally executed')

try_it(10.7)
try_it('Python')
'''
#Raise our own exception
'''
while True:
    x = (input("Enter an integer: "))
    if x < 0:
        raise Exception("Sorry no numbers below 0")
    if not type(x) is int:
        raise Exception("Must be an integer")
'''

# 5/7/24 #
#Object-Oriented Programming
'''
A class is used to create objects, a class is like a blueprint: one class can create multiple objects
Objects have fields and methods
Fields are  :can be public, everyone can see it, or private, hidden and no one can change it
Methods are 
Encapsultion is hiding the data from the rest of the program
Setters set someting
Getters return something



class Animal: #Creates the class; like a blueprint
    #Accessors
    def show_species(self): #Method
        print("I'm just a regular animal")
    def make_sound(self):
        print("Grrrr")
my_animal = Animal() # This creates a new animal OBJECT using the defult constructor

print("Here is infor about an animal")
my_animal.show_species()
my_animal.make_sound()


#Initializing Class objects: Method __init__

def __init__(self):
    print("I am an animal")
    self.name = "Gorilla" #No underscores means its public
    self.__age = '13' #2 underscores means its private, cannot be modified
    self._gender = 'female' # 1 underscore means its protected, only accessed within the package

# A super class or base class is the top class that inheritence come from
class Dog(Animal):
    def show_species(self):
        print("I am a dog")
    def make_sound(self):
        print("Woof! Woof!")
class Cat(Animal):
    def show_species(self):
        print("I am a cat")
    def make_sound(self):
        print("Meow! Meow!")
my_dog = Dog()
my_cat = Cat()

print("Here is some info about a dog")
my_dog.show_species()
my_dog.make_sound()
print("Here is some info about a cat")
my_cat.show_species()
my_cat.make_sound()

class Car:
    def set_year(self, year):
        self.year = year #public
    def set_make(self, make):
        self.__make = make #private
    def get_year(self):
        return self.year
    def get_make(self):
        return self.__make
    
mycar = Car()
mycar.set_year('2002')
mycar.set_make('Ford')
print('The year of the car is ', mycar.year) #Will print for public objects
print("The make of the car is ", mycar.get_make()) #Will print for private objects


'''
# 10/1/24 #
#Object Oriented Programming
'''
Class: Blueprint for what you can do

#Non programming
    Dog #Clause

    #Has a
        name
        bread
        birthday

    #Can do
        bark()
        bite()
        eat()
    
#To create dog

puppy1 is of type Dog() #puppy1 is an instance/object of the clause Dog

puppy1 = Dog()
puppy1.name = 'Spot'
puppy1.bread = 'Labrador'

puppy1.bark()

from decimal import Decimal

class Account:
    #Account class for maintaining a bank acount balance

    def __init__(self, name, balance, phoneNumber):
        #Initialize an Account object

        if balance < Decimal('0.00'):
            raise ValueError("Initial ballence must be >= to 0.00")
        
        self.name       = name
        self._balance    = balance
        self.phone      = phoneNumber
        

    def deposite(self, amount):
        #Deposit money into account

        if amount < Decimal('0.00'):
            raise ValueError("amount must be positive")
        
        self._balance += amount

    def getBalance(self):

        return(self._balance)

def main():
    print("Looking at Acount\n")

    account1 = Account('John Green', Decimal('50.00'), '456-9876')

    print("The account of", account1.name, 'is:', account1.getBalance())

    print("The account of", account1.name, 'is:', account1._balance)
    

main()
'''
'''
class Person:
    #Person class for future work

    def __init__(self, firstName, lastName, ID, email, phoneNumber):
        self.firstName   = firstName
        self.lastName    = lastName
        self.ID          = ID
        self.email       = email
        self.phoneNumber = phoneNumber


def main():

    person1 = Person('George', 'Washington', 1234, 'g.washington@email.edu', '555-555-0123')

    print("Instance created for", person1.firstName, person1.lastName)


main()

'''

# 5/9/24 #
'''
class CellPhone():
    def set_manufacturer(self, manufact):
        self.__manufacturer = manufact
    def set_model_number(self, model):
        self.__model_number = model
    def set_phone_price(self, price):
        self.__phone_price = price
    def get_manufacture(self):
        return self.__manufacturer
    def get_model_number(self):
        return self.__model_number
    def get_phone_price(self):
        return self.__phone_price
myPhone = CellPhone()
myPhone.set_manufacturer('AT&T')
myPhone.set_model_number('iPhone 12')
myPhone.set_phone_price('$600')
print("My phone provider is ", myPhone.get_manufacture())
print("My phone's model number is ", myPhone.get_model_number())
print("My phone's price is ", myPhone.get_phone_price())

# test_doctest.py
# see if doctest works with the testmod

x = 5

def squared(x):
    """ return the squared value of x
    >>> squared(5)
    25
    """
    return x*x

print(f'Your number {x} squared: {squared(x)}')

import doctest
doctest.testmod(verbose=True)

import math

numbers = [1,2,3,4,5]

print(numbers ** 2)
'''

#CIS 131#

# 9/17/24 #
#Dictionaries

'''
# '1' is the key, 'Patrick' is the value
myDictionary = {1: 2 , 2 : ['Everyone', 'else']}

#Updating a dictionary
myDictionary[2] = 'Whatever'
print(myDictionary)

#Adding to a dictionary
myDictionary['Samus'] = .007 #Keys can be different types

myDictionary[2] = ['Everyone', 'else']

#Print just the value
print(myDictionary[2]) 

#Updating a list within a dictionary
myDictionary[2][1] = 'elsewhere'
print(myDictionary)

# Getting only keys or values and turning them into a list
print(list(myDictionary.values()))

#itterating over the dictionary

for key, value in myDictionary.items():
    print(f'{key} is connected to {value}')
'''
