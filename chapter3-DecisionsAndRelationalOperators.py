##
# This program simulates an elevator
##

# Obtain the floor number from the user as an integer
floor = int(input("Enter the floor: "))

if floor > 13:
    actualFloor = floor - 1
else:
    actualFloor = floor

print("The elevator will travel to the actual floor", actualFloor)
# Compare strings

name1 = input("Enter your name")
name2 = input("Re-Enter your name")
if name1 == name2:
    print("Name matched")
else:
    print("Name not matched")

##
# This program demonstrates comparisons of numbers, using Boolean expressions.
#
x = float(input("Enter a number (such as 3.5 or 4.5): "))
y = float(input("Enter a second number: "))
if x == y:
    print("They are the same.")
else:
    if x > y:
        print("The first number is larger")
    else:
        print("The first number is smaller")
    if -0.01 < (x - y) < 0.01:
        print("The numbers are close together")
    if x == y + 1 or x == y - 1:
        print("The numbers are one apart")
    if x > 0 and y > 0 or x < 0 and y < 0:
        print("The numbers have the same sign")
    else:
        print("The numbers have different signs")

# Lab 3 Exercise

# Exercise 1

number1 = int(input("Enter the first number"))
number2 = int(input("Enter the second number"))
number3 = int(input("Enter the third number"))

if number1 < number2 < number3:
    print("The numbers are in ascending order")
elif number1 > number2 > number3:
    print("The numbers are in descending order")
else:
    print("The numbers are out of order")

# Exercise 2
season = ""
activity = ""
month = input("Enter month of the year")

if month.lower() in "december, january, february":
    season = "Winter"
    activity = "Snowboarding"
elif month.lower() in "march, april, may":
    season = "Spring"
    activity = "Hiking"
elif month.lower() in "june, july, august":
    season = "Summer"
    activity = "Swimming"
elif month.lower() in "september, october, november":
    season = "Summer"
    activity = "Swimming"
else:
    season = " "
    activity = " "

if season.isspace() and activity.isspace():
    print("Month entered is invalid")
else:
    print("In", month, "it is", season,", I suggest you go", activity)

# Exercise 2 repeat
season = ''
activity =''
month = input("Enter the month of the year")
month = month.lower()
if month in ('march', 'april', 'may'):
    season = 'spring'
    activity = 'hiking'
elif month in ('december', 'january', 'february'):
    season = 'winter'
    activity = 'snowboarding'
elif month in ('june', 'july', 'august'):
    season = 'summer'
    activity = 'swimming'
elif month in ('september', 'october', 'november'):
    season = 'autumn'
    activity = 'biking'
else:
    print("Month entered is invalid")
    exit()
print("In", month.capitalize(), ", it is", season.capitalize(), ", I suggest you go", activity.capitalize())
print("In %s, it is %s, I suggest you go %s" %(month.capitalize(),season.capitalize(),activity.capitalize()))

# Samples from slide
string = "http://csd.uwo.ca/courses/intro.html"
fileextn = ".html"
fileextn in string # True
string.endswith('.html') #True

sentence = "The fox went to see an ox on an oxcart bulit by a fox"
substring ="ox"
sentence.count(substring) # ans: 4

sentence = "The fox went to see an ox on an oxcart bulit by a fOx"
substring ="ox"
sentence.count(substring) #ans: 3
sentence.startswith('The') # true
sentence.startswith('the') # false


sentence = "GeeksforGeeksforGeeksforGeeks"
substring ="GeeksforGeeks"
sentence.count(substring)   #ans: 2
sentence.startswith('for') # false
sentence.find('ks')     #ans: 3

s = "123"
s.isalnum() # True. Returns true if the string contains letters or digits
s.isalpha() # false
s.isdigit() # True

string = "jgkfjgkfjgk"
string.isupper()        # False
string.islower()        # True
string.isspace()        # False

'john' < 'John' # False since upper case J comes before lower case j

name = "john oh Johnson"
name.isalnum()      # false since it contains blank space too
name.isalpha()      # false since it contains blank space too

"-1726".isdigit()   #false since negative sign is not a digit


## ternary operator in python for if else

is_bored = True
state = "Watching TV" if is_bored else "working"
print(state)

## Implementing switch case with python
# Python does not have any inbuilt switch case like c# or Java
# So to implement a switch-case, you can either use if-elsif-else ladder
# or implement a dictionary mapping function

def week(i):
    switcher = {
        0:'Sunday',
        1:'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
    }
    return switcher.get(i ,"Invalid day of the week")

week(2)
