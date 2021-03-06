##################################### Lists ############################

moreValues = []
print(moreValues)

values = [32, 54, 67, 29, 35, 80, 115]
print(values[0], values[3])

values[5] = 81 # You can change values in a list. Lists are mutable.
values = values + [19.8]
print(values)

str = "Hello"
print(str)
str[1] = 'a'    # Error. String does not support item assignment. Strings are immutable.
print(str)

##################### Accessing lists using for Loops #####################

values = [32, 54, 67.5, 29, 35, 80, 115, 44.5, 100, 65]

for i in range(10):
    print(i, values[i])

for i in range(len(values)):
    print(i, values[i])

for item in values:
    print(item)

##################### List aliases #######################

scores = [10, 9, 7, 4, 5]
values = scores
values == scores  # True. Since both scores and values point to the same address in memory.

print(scores[-1]) # prints last element in the list.

################### List Operations #########################

#### Appending

# create empty list
friends = list()

# append elements
friends.append("Harry")
friends.append("Emily")
friends.append("Bob")
friends.append("Cari")
print(friends)

# insert elements at specific position
friends.insert(1, "Mike")
print(friends)

######## Finding an element
# use in operator to find an element in teh list

if "Emily" in friends:
    print("She is a friend")

# use index to find the position of an element
friends = ["Harry", "Emily", "Bob", "Cari", "Emily"]
n = friends.index("Emily")
print(n)                    # Output: 1. Returns the position of first encountered "Emily"


######### Removing an element
# pop() method removes the element at a given position
# All of the elements following the removed element are moved up
# one position to close the gap. The length of the list is reduced by 1

friends = ["Harry", "Emily", "Bob", "Cari", "Bill"]
friends.pop(1)      # removes element at index 1
print(friends)      # Output: ['Harry', 'Bob', 'Cari', 'Bill']
friends.pop()       # removes last element from the list
print(friends)      #Output: ['Harry', 'Bob', 'Cari']

# remove() method removes the given element from the list
friends.remove("Bob")
print(friends)      # ['Harry', 'Cari']

######## Concatenation
# concatenation of two lists is a new list that contains the elements
# of the first list, followed by the elements of the second.
# Two lists can be concatenated by using the plus (+) operator

myFriends = ["Fritz", "Cindy"]
yourFriends = ["Lee", "Pat", "Phuong"]

ourFriends = myFriends + yourFriends
print(ourFriends)               # Output: ['Fritz', 'Cindy', 'Lee', 'Pat', 'Phuong']

########### Replication
# The integer specifies how many copies of the list should be concatenated.
# One common use of replication is to initialize a list with a fixed value
monthInQuarter = [1, 2, 3] * 4
print(monthInQuarter)           # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

monthyScores = 4 * [0]
print(monthyScores)             # Output: [0, 0, 0, 0]

############### Equality and Inequality testing
# You can use the == operator to compare whether two lists have the
# same elements, in the same order.

[1, 4, 9] == [1, 4, 9]  # Output: True
[1, 4, 9] == [1, 9, 4]  # Output: False

[1, 4, 9] != [ 4, 9]    # Output: True


############### Sum, Maximum, Minimum
sumOfItems =  sum([1, 4, 9, 16])           # Answ: 30
print(sumOfItems)
maximum = max([1, 4, 9, 16])               # Ans: 16
print(maximum)
minimum = min([1, 4, 9, 16])               # Ans: 1
print(minimum)
min("Fred", "Ann", "Sue")                  #Ans: Ann


############### Sorting
values = [1, 16, 9, 4]
print(values)
print(values.sort())    # prints None. Since sort method sorts values and the sorted values are in the original list
print(values)           # Output: [1, 4, 9, 16]

############## Copying lists
values = [1, 16, 9, 4]
# prices and values have the same reference now.
prices = values

# Sometimes, you want to make a copy of a list; that is, a new list that
# has the same elements in the same order as a given list. Use the list() function
newprices = list(values)

############## Slicing lists
temperatures = [18, 21, 24, 33, 39, 40, 39, 36, 30, 22, 18]
print(temperatures[6:9])    # Output: [39, 36, 30]. From index 6 to index 8. Does not include 9

t1 = temperatures[6:9]
print(t1)                    # Output: [39, 36, 30]. From index 6 to index 8. Does not include 9

t2 = temperatures[:6]
print(t2)                    # Output: [18, 21, 24, 33, 39, 40]. From index 0 to 5.

t3 = temperatures[7:]
print(t3)                    # Output: [36, 30, 22, 18]. From index 7 to end of the list

temperatures[6: 9] = [45, 44, 40] # Replaces the values in elements 6, 7, and 8
print(temperatures)                 # Output: [18, 21, 24, 33, 39, 40, 45, 44, 40, 22, 18]

########################## Common List Algorithms #########################

########## Filling a List
numbers = list()
for i in range(10):
    numbers.append(i*i)
print(numbers)

############# Combining list elements
## Computer sum of elements
numbers = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
result = 0.0
for element in numbers:
    result = result + element
print(result)
print(sum(numbers)) # this way is also valid.

## Concatenate strings
names = ["Harry", "Sally", "Goldy", "Cari"]
result = ""
for element in names:
    result = result + element
print(result)

## Element separators

names = ["Harry", "Sally", "Goldy", "Cari"]
result = ""
for element in names:
    result = result + element + ","
print(result)

# If you want to print without adding value to string
names = ["Harry", "Sally", "Goldy", "Cari"]
for i in range(len(names)):
    if i > 0:
        print("| ", end="")
        print(names[i], end="")
    else:
        print(names[i], end="")

names = ["Harry", "Sally", "Goldy", "Cari"]
for element in names:
    print(element, end="")
    print("| ", end="")

########### Find Maximum and Minimum values from the list
values = [44, 56.2, 2, 1.4, 78, 90.3, 34, 9]
smallest = None
largest = None
for element in values:
    if smallest is None or element < smallest:
        smallest = element
    if largest is None or element > largest:
        largest = element
print("The minimum value in the given list is", smallest)
print("The maximum value in the given list is", largest)

# This method initialize smallest and largest to first value in the list
values = [44, 56.2, 2, 1.4, 78, 90.3, 34, 9]
smallest = values[0]
largest = values[0]
for element in values:
    if element < smallest:
        smallest = element
    if element > largest:
        largest = element
print("The minimum value in the given list is", smallest)
print("The maximum value in the given list is", largest)

########### Linear Search
# Finding the first value that is > 100
values = [44, 56.2, 2, 1.4, 78, 103.3, 34, 119]
limit = 100
found = False
pos = 0
while pos < len(values) and not found:
    if values[pos] > limit:
        found = True
    else:
        pos += 1
if found:
    print("The first element > 100 found at position", pos)
else:
    print("No elements > 100 found")

# Collecting all matches
values = [44, 56.2, 2, 1.4, 78, 103.3, 34, 119]
results = list()
limit = 100
found = False
pos = 0
while pos < len(values):
    if values[pos] > limit:
        results.append(values[pos])
    pos += 1
print(results)

# Counting all values > 100
values = [44, 56.2, 2, 1.4, 78, 103.3, 34, 119]
limit = 100
count = 0
pos = 0
while pos < len(values):
    if values[pos] > limit:
        count += 1
    pos += 1
print(count)

# Removing matches
# Remove all elements that match a particular condition.
# Remove all words with length > 4

words = ["Penguin", "Apple", "Fox", "Fish", "Tractor", "Yoyo"]
print(words)
for word in words:
    if len(word) > 4:
        words.remove(word)
print(words)

# Another method
words = ["Penguin", "Apple", "Fox", "Fish", "Tractor", "Yoyo"]
print(words)
i = 0
while i < len(words):
    if len(words[i]) > 4:
        words.pop(i)
    i += 1
print(words)

# Swapping values in two lists
words1 = ["Penguin", "Apple", "Fox"]
words2 = ["Fish", "Tractor", "Yoyo"]

temp = words1[1]
words1[1] = words2[1]
words2[1] = temp

# Reading input into list
namelist = list()
name = input("Enter name of your friends: Press space to quit")
#while not name.isspace():
while name != '':
    namelist.append(name)
    #name = input("Enter name of your friends: Press space to quit")
    name = input("")
print("The list of names entered are:", namelist)


######################## Using Lists with functions ###############

## function the accepts list as argument
def sum(values):
    total = 0
    for element in values:
        total = total + element
    return total
tot = sum([34, 56, 18, 90])
print(tot)

## function that multiples list elements by a given factor
# This function modifies the list inside the function
def multiply(values, factor):
    for i in range(len(values)):
        values[i] = values[i] * factor
    return values

numlist = [4, 3, 5, 7]
print(numlist)          # Output: [4, 3, 5, 7]
multiply(numlist, 5)
print(numlist)          # Output: [20, 15, 25, 35]


# This function returns the modified list.
def multiply(values, factor):
    for i in range(len(values)):
        values[i] = values[i] * factor
    return values

vallist = multiply([4, 3, 5, 7], 5)     # output: [20, 15, 25, 35]. Both vallist and the list passed is pointing to same memory location
print(vallist)

newnumlist = list()
newnumlist = multiply([4, 3, 5, 7], 5)
print(newnumlist)           # output: []. Here newnumlist is a list new and its reference is a new location not same as list passed.

##### Reverse function

## read float numbers, modify list and then reverse print the list
def read_float(numberOfInputs):
    inputNumbers = []
    for i in range(numberOfInputs):
        value = float(input("Enter float value"))
        inputNumbers.append(value)
    return inputNumbers


def multiply(values, factor):
    for i in range(len(values)):
        values[i] = values[i] * factor

# range syntax : range(stop) or range(start, stop) or range(start, stop. step)
def reversePrintList(values):
    for i in range(len(values)-1, - 1, -1):
        print(values[i], end=",")

def main():
    inputvalues = read_float(5)
    print(inputvalues)
    multiply(inputvalues, 2)
    reversePrintList(inputvalues)

main()

### Returning multiple values using tuple
# all operations that can be performed on a list can be applied on a tuple except ones that modify the list.
# Tuples are immutable (cannot be modified)

def readDate():
    print("Enter a date")
    day = int(input("Enter day"))
    month = input("Enter month")
    year = int(input("Enter year"))
    return (day, month, year)

# print(readDate())
date = readDate()
print(date)
print(type(date))

#### Using tuple for varying number of arguments
### In the below code, *values refer to a tuple. It can accept any number of values.

def sumOfNumbers(*values):
    total = 0
    for element in values:
        total = total + element
    return total

print(sumOfNumbers(2,3,6,8,9,22))
print(sumOfNumbers(50,25,15,10))


#### Return List from a function. This function accepts a number n and generate squares of first n numbers in a list.
def squares(n):
    result = list()
    for i in range(n):
        result.append(i * i)
    return result

num = int(input("Enter an integer"))
squareList = squares(num)
print("The squares of numbers till", num,"are", squareList)

## Find the quiz score from a series of scores after dropping lowest 2 values.

def readFloat():
    quizScores = list()
    quizScore = input("Enter the score. Press 'Q' to exit entering values")
    while quizScore != 'Q':
        quizScores.append(float(quizScore))
        quizScore = input("Enter the score. Press 'Q' to exit entering values")
    return quizScores


def dropLowestScore(scores):
    scoresList = list(scores)
    posOfSmallestScore = 0
    for i in range(len(scoresList)):
        if scoresList[i] < scoresList[posOfSmallestScore]:
            posOfSmallestScore = i
    scoresList.pop(posOfSmallestScore)
    return scoresList


def main():
    scores = readFloat()
    print(scores)
    if len(scores) > 1:
        scores_afterdrop = dropLowestScore(scores)
        scores_afterdrop = dropLowestScore(scores)
        total = sum(scores_afterdrop)
        print("The final score is", total)
    else:
        print("Not enough values for calculating quiz scores")


main()

### This program counts the dice toss values and print how many times each value appeared.

## This function reads die tosses and counts the number of times each value appeared
def countInputs(sides):
    minSideValue = 1
    maxSideValue = 6
    tossValueCount = [0] * (sides + 1)
    userInput = input("Enter the die value. Press Q to quit")
    while userInput != 'Q':
        inputValue = int(userInput)
        if inputValue >= 1 and inputValue <= 6:
            tossValueCount[inputValue] = tossValueCount[inputValue] + 1
        else:
            print("Invalid user input")
        userInput = input("Enter the die value. Press Q to quit")
    return tossValueCount

def printCounters(tossValues):
    for i in range(1,len(tossValues)):
        print("%2d: %4d" % (i, tossValues[i] ))

def main():
    counters = countInputs(6)
    printCounters(counters)


main()

####### Tables ########
# A table/matrix  can be created using 2 dimensional lists.
# In the below code, counts is a table/matrix with 8 rows and 3 columns
counts = [
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 1],
    [3, 1, 1],
    [0, 1, 0],
    [1, 0, 1],
]

print(counts)
for i in counts:
    print(i)


# Initialize a table with 8 rows and 3 columns
ROWS = 8
COLUMNS = 3
table = []
for i in range(ROWS):
    table.append([0] * COLUMNS)
print(table)

# This program prints a table of medal winner counts with row totals
MEDALS = 3
COUNTRIES = 8

# Create a list of countries
countryNames = ["Canada",
                "Italy",
                "Germany",
                "Japan",
                "Norway",
                "Russia",
                "USA",
                "Sweden"]

# create a table of medal counts
counts = [
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 1],
    [3, 1, 1],
    [0, 1, 0],
    [1, 0, 1],
]

# print table header

print("%15s %8s %8s %8s %8s" % ('Country', 'Gold', 'Silver', 'Bronze', 'Total'))
for i in range(COUNTRIES):
    print("%15s" % countryNames[i], end='')
    total = 0
    for j in range(MEDALS):
        print("%8d" % counts[i][j], end='')
        total = total + counts[i][j]
    print("%8s" % total)

### Lab exercises 1
# Write a program that reads numbers and adds them to a list if they aren’t already
# contained in the list. When the list contains ten numbers, the program displays the
# contents and quits.

def main():
    valuelist = list()
    while len(valuelist) <= 10:
        userinput = input("Enter a number:")
        if userinput.isdigit():
            valueinput = int(userinput)
            if valueinput not in valuelist:
                valuelist.append(valueinput)
        else:
            print("Invalid number")
    print("The numbers entered are:", valuelist)


main()


### Lab exercises 2
# Write a program that generates a sequence of 20 random values between 0 and 99 in a
# list, prints the sequence, sorts it and prints the sorted sequence. Use the list sort
# method.

from random import randint
COUNT = 20
LOWER_LIMIT = 0
UPPER_LIMIT = 99
sequenceList = list()
for i in range(COUNT):
    randomvalue = randint(0, 99)
    sequenceList.append(randomvalue)
print("The random sequence generated: ", sequenceList)
sequenceList.sort()
print("The sorted sequence:", sequenceList)

### List comprehensions
## List comprehensions are an elegant way to build a list without having to use
# different for loops to append values one by one.

# syntax: expression-involving-loop-variable for loop-variable in sequence

# list of integers from 0 to 9
listOfNums = [x for x in range(10)]
print(listOfNums)   # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [ expression-involving-loop-variables for outer-loop-variable in outer-sequence
# for inner-loop-variable in inner-sequence ]

# To generate all combinations of lists [1,2,3] and [4,5,6]

results = []
for x in [1,2,3]:
    for y in [4,5,6]:
        results.append([x, y])
print(results)  # output: [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]

# the above code is equivalent to below list comprehension

print([[x,y] for x in [1,2,3] for y in [4,5,6]])
# output: [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]

## list comprehension involves creating a list and filtering it similar to using the filter() method.
# The filtering of list comprehension takes the following form
#[ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ]
# This form is similar to the simple form of list comprehension, but it evaluates boolean-expression-involving-loop-variable
# for every item.
# It also only keeps those members for which the boolean expression is True.

## Print of list of numbers within 10 that are multiples of 3
listOfThreeMultiples = [x for x in range(10) if x % 3 == 0]
print(listOfThreeMultiples)
# output: [0, 3, 6, 9]

## Print the sqaures of a list of number using list comprehension

# function to computer square of a number
def square(num):
    return num**2

listOfNums = range(1,11)
print([square(x) for x in listOfNums])

listOfNums = range(1, 11)
listOfSquares = [square(x) for x in listOfNums]
print(listOfSquares)

# another way to use list comprehension to find squares of numbers
list1 = [x * x for x in range(11)]
print(list1)

# another way to use list comprehension to find squares of numbers and print the ones greater than 25
list1 = [x * x for x in range(11) if x * x > 25]
print(list1)