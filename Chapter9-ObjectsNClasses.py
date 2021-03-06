############################## Objects and classes ##########################
###################### Example 1 ########################
# class Counter:
#     ## Gets current value of this container
#     # @return the current value
#     #
#     def getValue(self):
#         return self._value
#
#     ## Advances teh value of this counter by 1
#     #
#     def click(self):
#         self._value = self._value + 1
#
#     ## Resets the value of this counter to 0
#     #
#     def reset(self):
#         self._value = 0
#
#
# tally = Counter()
# tally.reset()
# tally.click()
# tally.click()
#
# result = tally.getValue()
# print("Value:", result)
#
# tally.click()
# result = tally.getValue()
# print("Value:", result)

# ###################### Example 2 ########################
# class CashRegister:
#     # constructor
#     def __init__(self):
#         self._itemCount = 0
#         self._total = 0.0
#
#     ## Adds an item to this cash register
#     # @param price: thee price of this item
#     #
#     def addItem(self, price):
#         self._itemCount += 1
#         self._total = self._total + price
#
#     ## Gets current total of this container
#     # @returns the  total
#     #
#     def getTotal(self):
#         return self._total
#
#     ## Gets current item count of this container
#     # @returns the item count
#     #
#     def getCount(self):
#         return self._itemCount
#
#     ## Resets the value of item count and total to 0
#     #
#     def clear(self):
#         self._itemCount = 0
#         self._total = 0
#
#
# register1 = CashRegister()
# register1.clear()
# register1.addItem(1.29)
# register1.addItem(6.99)
# register1.addItem(7.99)
# total = register1.getTotal()
# count = register1.getCount()
# print("Items purchased: %2d. Total price: % 5.2f" %(count, total))
######################################## Fraction class ##########################

# ## Find the greatest common divisor (GCD) of two numbers using simple method
# # return GCD
#
# def GCD(num1, num2):
#     if num1 > num2:
#         temp = num1
#         num1 = num2
#         num2 = num1
#     for x in range(num1, 0, -1):
#         if num1 % x == 0 and num2 % x == 0:
#             return x
#
# print(GCD(15, 20))
#
# ## Find the greatest common divisor (GCD) of two numbers using euclidian method
# # return GCD
#
# def GCD_euclid(a, b):
#     if a < b:
#         temp = a
#         a = b
#         b = temp
#     while a % b != 0:
#         tempA = a
#         tempB = b
#         a = tempB
#         b = tempA % tempB
#     return b
#
# print(GCD_euclid(15, 20))
# print(GCD_euclid(2, 4))
#
# ## Fraction class constrcutor
# #
# #
# class Fraction:
#     def __init__(self, numerator=0, denominator=1):
#         if denominator == 0:
#             raise ZeroDivisionError("Denominator cannot be zero")
#         if numerator == 0:
#             self._numerator = 0
#             self._denominator = 1
#         else:
#             if (numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0):
#                 sign = -1
#             else:
#                 sign = 1
#             a = abs(numerator)
#             b = abs(denominator)
#
#             # finding GCD to reduce fraction to the simplest form
#             if a < b:
#                 temp = a
#                 a = b
#                 b = temp
#             while a%b != 0:
#                 tempA = a
#                 tempB = b
#                 a = tempB
#                 b = tempA % tempB
#             self._numerator = abs(numerator) // b * sign
#             self._denominator = abs(denominator) // b
#             #print(self._numerator, "/", self._denominator)
#
#
# # Test
# frac1 = Fraction(1, 8)
# frac1 = Fraction(-2, -4)
# frac1 = Fraction(-2, 4)
# frac1 = Fraction(3, -7)
# frac1 = Fraction(0, 15)
# frac1 = Fraction(8, 0)

################################ Lab 10 - Exercise #############################

class Car:

    # constructor
    def __init__(self, efficiency=1):
        self._efficiency = efficiency
        self._fuelLevel = 0.0

    # Drive method uses fuel based on distance driven
    # @param miles - distance driven
    #
    def drive(self, miles):
        self._fuelLevel = self._fuelLevel - (miles/self._efficiency)

    # Add fuel level
    # @ param fuel - fuel in gallons
    #
    def addGas(self, fuel):
        self._fuelLevel = self._fuelLevel + fuel

    # Get current gas level
    # return fuel level
    def getGasLevel(self):
        return self._fuelLevel




def main():
    # myHybrid = Car(50)
    # myHybrid.addGas(20)
    # print("Gaslevel from class",myHybrid.getGasLevel())
    # print("Expected gas level: 20")
    # myHybrid.drive(100)
    # print("Gaslevel from class",myHybrid.getGasLevel())
    # print("Expected gas level: 18")
    efficiency = input("Enter fuel efficiency of your car")
    gaslevel = input("Enter the amount of fuel filled")
    distance = input("Enter the distance travelled")
    myHybrid = Car(int(efficiency))
    myHybrid.addGas(float(gaslevel))
    print("Gaslevel from class", myHybrid.getGasLevel())
    myHybrid.drive(float(distance))
    print("Gaslevel from class",myHybrid.getGasLevel())


main()