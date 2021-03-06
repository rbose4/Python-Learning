# Chapter 4 - Loops

# # Average of numbers given numbers
done = False
count = 0
average = 0.0
total = 0.0
while not done:
     inputstr = input("Enter a number or enter -1 to exit")
     if len(inputstr) == 0:
         print("Enter a number")
         continue
     elif inputstr == "-1":
         done = True
     else:
         try:
             total = total + float(inputstr)
             count += 1
         except:
             print("The value entered is not valid", inputstr)
 if count > 0:
     average = total/count
 else:
     average = 0.0
 print("Average of %d numbers is %f" %(count, average))

# # Sum of n numbers
 total = 0.0
 count = 0
 inputstr = input("Enter a number. Press space to exit")
 while not inputstr.isspace():
     try:
         number = float(inputstr)
         total = total + number
         count += 1
     except:
         print("Invalid number", inputstr)
         exit()
     inputstr = input("Enter a number")
 print("Sum of %d numbers is %f" % (count, total))

# # Count the number of negative values
# negatives = 0
# inputstr = input("Enter a value. Press enter to exit")
# while inputstr != "":
#     try:
#         value = float(inputstr)
#         if value < 0:
#             negatives += 1
#     except:
#         print("Invalid number", inputstr)
#     inputstr = input("Enter a value. Press enter to exit")
# print("%d negatives values were entered" %negatives)

# # Find the largest and smallest values in the list of numbers entered
# largest = 0
# smallest = 0
# inputstr = input("Enter a value. Press enter to exit")
# while inputstr != "":
#     try:
#         value = float(inputstr)
#         if value > largest:
#             largest = value
#         if value < smallest:
#             smallest = value
#     except:
#         print("Invalid number", inputstr)
#     inputstr = input("Enter a value. Press enter to exit")
# print("The largest value so far is", largest)
# print("The smallest value so far is", smallest)
############## FOR LOOP ##################################

# for i in range(0, 12, 2):
#     print(i)                # Output 0, 2, 4, 6, 8, 10
#     
# # Find the sum of all even numbers between 0 and the number entered
# sum = 0.0
# inputstr = input("Enter the number")
# number = int(inputstr)
# for i in range(0, number, 2):
#     sum = sum + i
# print("The sum of even numbers between 0 and %d is %f" %(number, sum))
#
# # Powertable x^1 to x^4 for numbers 1 to 10
#
# rowMax = 10
# colMax = 4
# value = 0.0
# # print table header
# for n in range(1, colMax + 1):
#     print("%10d" % n, end="")
# print()
# for i in range(1, colMax + 1):
#     print("%10s" % "x ", end="")
# print()
# string = '-' * 60
# print("%10s" % string)
#
# # print values
# for x in range(1, rowMax + 1):
#     for n in range(1, colMax + 1):
#         value = x ** n
#         print("%9d " % value, end="")
#     print()

# ## Prints checker board pattern
#
# for i in range(3):
#     for j in range(5):
#         if i % 2 == j % 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
###################################################################
# # Lab exercise
# smallest = 0.0
# largest = 0.0
# total = 0
# count = 0
# inputstr = input("How many numbers do you wish to use today?")
# noofnumbers = int(inputstr)
# while count < noofnumbers:
#     num = float(input("Enter the number"))
#     count += 1
#     if num > largest:
#         largest = num
#     if smallest == 0.0 or num < smallest:
#         smallest = num
#     total = total + num
# print("The average of the values is", total/count)
# print("The smallest of the values is", smallest)
# print("The largest of the values is", largest)
# print("The range of the values is", largest - smallest)
######################################################################
# # Count the upper case letters and vowels in a string
# count_upper = 0
# count_vowel = 0
# inputstr = input("Enter the string:")
# for char in inputstr:
#     if char.isupper():
#         count_upper += 1
#     if char.lower() in "aeiou":
#         count_vowel += 1
# print("The string %s has %d vowels and %d upper case letters" %(inputstr, count_vowel, count_upper))
#
###################################################
# # Print the position of each upper case letters
#
# inputstr = input("Enter the string:")
# for i in range(len(inputstr)):
#     if inputstr[i].isupper():
#         print(i)
######################################################
# # Print the postion of first digit in a string
# position = 0
# inputstr = input("Enter the string:")
# for i in range(len(inputstr)):
#     if inputstr[i].isdigit():
#        position = i
#        break
# if position != 0:
#     print("First digit occurs at position", position)
# else:
#     print("The string does not contain a digit", position)
# ############################################################
# # Print the postion of last digit in a string
# position = 0
# inputstr = input("Enter the string:")
# for i in range(len(inputstr)-1, 0, -1):
#     if inputstr[i].isdigit():
#         position = i
#         break
# if position != 0:
#     print("Last digit occurs at position", position)
# else:
#     print("The string does not contain a digit", position)

# ############################################################
# # Validate a string format
# # With loop
# text = input("Enter a phone number in the format (###)###-####")
# text = text.strip()
# valid = len(text) == 13
# position = 0
# while valid and position < len(text):
#     if position == 0:
#         valid = text[0] == '('
#     elif position == 4:
#         valid = text[4] == ')'
#     elif position == 8:
#         valid = text[8] == '-'
#     else:
#         valid = text[position].isdigit()
#     position += 1
# if valid:
#     print("The string contains a valid telephone number")
# else:
#     print("Invalid!!! The string does not contain a valid telephone number")

# ### Short version of the above code
# text = input("Enter a phone number in the format (###)###-####")
# #ext = "(519)868-6625"
# valid = len(text) == 13
# position = 0
# while valid and position < len(text):
#     valid = ((position == 0 and text[position] == "(")
#              or (position == 4 and text[position] == ")")
#              or (position == 8 and text[position] == "-")
#              or (position != 0 and position != 4 and position != 8 and text[position].isdigit()))
#     position += 1
# if valid:
#     print("The string contains a valid telephone number")
# else:
#     print("Invalid!!! The string does not contain a valid telephone number")

# # With regular expression
# import re
# text = input("Enter a phone number in the format (###)###-##")
# text = text.strip()
# if re.search('\(\d\d\d\)\d\d\d-\d\d\d',text):
#     print("The string contains a valid telephone number")
# else:
#     print("Invalid!!! The string does not contain a valid telephone number")
#
######################################################################
## Applying Random numbers
import random

for i in range(10):
    d1 = random.randint(1, 6)      # 1 and 6 included
    d2 = random.randint(1, 6)
    d3 = random.random()    # generate random float between 0 and 1 ( 0 <= r < 1 )
    print(d1, d2, d3)

## Monte Carlo method
# This program computes an estimate of pi by simulating dart throws onto a square

from random import random
TRIES = 10000

hits = 0
for i in range(TRIES):
    # Generate two random number between 1 and -1.
    # r = randon(); x = a + (b - a) * r where a <= x < b
    r = random()
    x = -1 + 2 * r
    r = random()
    y = -1 + 2 * r

    # check if the point lies in th unit circle
    if x * x  + y * y <= 1:
        hits += 1
 # The ratio hits/tries is approximately the same as th ratio circle area/ square area = pi/4
piEstimate = 4.0 * hits / TRIES
print("Estimate for pi:", piEstimate)

