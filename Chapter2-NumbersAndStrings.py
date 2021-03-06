from math import sqrt
import math

# Calculate the volume of cans and bottle

# Liters in 12-ounce can
CAN_VOLUME = 0.355
# Liters in a two-liter bottle
BOTTLE_VOLUME = 2

# Number of cans per pack
cansPerPack = 6

# Calculate total volume in the cans
totalVolume = cansPerPack * CAN_VOLUME
print("A six-pack of 12-ounce cans contains", totalVolume, "liters")
# Calculate total volume in the cans and a 2-liter bottle.
totalVolume = totalVolume + BOTTLE_VOLUME
print("A six-pack and a two-liter bottle contain", totalVolume, "liters.")

# Convert pennies to dollars
pennies = 1729
dollars = pennies // 100
cents = pennies % 100
print("I have", dollars, "dollars and", cents, "cents.")

# Built-in functions
tax = 12.3
total = 1000
balance = total + tax
intbalance = int(balance)
print("Balance before int conversion is", balance, "and after conversion is", intbalance)

# Round of example

print("Before rounding", 10.5567, "after rounding is", round(10.5567, 3))
print("Max of 2,5,6,7,9 is", max(2, 5, 6, 7, 9))
print("Min of 2,5,6,7,9 is", min(2, 5, 6, 7, 9))

# Adding python libraries
y = sqrt(64)
print(y)

# round of errors

price = 4.35
quantity = 100
totalPrice = price * quantity
print(round(totalPrice, 2))

# Different
print(round(math.sin(90)))

firstName = "Roopa"
lastName = "Bose"
name = firstName + " " + lastName
print(name)
length = len(name)
print("Length of string is", length)

dashes = "-" * 50
print(name, dashes, ".")

# int/ float to string conversion
balance = 888.88
dollars = 888
balanceAsString = str(balance)
dollarsAsString = str(dollars)
print(balanceAsString)
print(dollarsAsString)

# string to int/float conversion
id = int("1729")
price = float("17.29")
print(id)
print(price)

# string functions
strName = "Roopa"
strFName = "Bose"

strName = strName.upper()
print(strName)
strFName = strFName.lower()
print(strFName)
strReplacedName = strName.replace("O", "0")
print(strReplacedName)

# Escape sequence
print("He said \"Hello\"")
print("C:\\Temp\\Secret.txt")

# Lab 2 Exercise

integer1 = int(input("Please enter first number"))
integer2 = int(input("Please enter second number"))

sumNumber = integer1 + integer2
product = integer1 * integer2
distance = abs(integer1 - integer2)
average = sumNumber / 2
maximum = max(integer1, integer2)

print("Sum: ", sumNumber)
print("Product: ", product)
print("Distance: ", distance)
print("Average: ", average)
print("Maximum: ", maximum)
print() # print new line
print()
# Printing formatted string

print("%-15s%-10d" % ("Sum: ", sumNumber))
print("%-15s%-10d" % ("Product: ", product))
print("%-15s%-10d" % ("Distance: ", distance))
print("%-15s%-10.2f" % ("Average: ", average))
print("%-15s%-10d" % ("Maximum: ", maximum))

print("%-10s%-5d" % ("Sum: ", sumNumber))
print("%-10s%-5d" % ("Product: ", product))
print("%-10s%-5d" % ("Distance: ", distance))
print("%-10s%-5.2f" % ("Average: ", average))
print("%-10s%-5d" % ("Maximum: ", maximum))

print("%-10s%5d" % ("Sum: ", sumNumber))
print("%-10s%5d" % ("Product: ", product))
print("%-10s%5d" % ("Distance: ", distance))
print("%-10s%5.2f" % ("Average: ", average))
print("%-10s%5d" % ("Maximum: ", maximum))