########################## Functions ###############################

# ############### Cube Volume ###############
# ## Computes the volume of a cube
# # @param sideLength the length of a side of the cube
# # @return the volume of the cube
# def cubeVolume(sideLength):
#     volume = sideLength ** 3
#     return volume
#
# ##
# # This program computes the volume of two cubes.
# #
# def main():
#     result1 = cubeVolume(2)
#     result2 = cubeVolume(10)
#     print("A cube with the length 2 has volume", result1)
#     print("A cube with the length 10 has volume", result2)
#
# # Call the main function to begin executing the program
# main()

############### pyramid volume ###############
# ## Computes the volume of a pyramid
# # @param height a float indicating the height of the pyramid
# # @param baselength a float indicating the length of one side of the pyramid's base
# # @return the volume of the pyramid as a float
#
# def pyramidVolume(height, baseLength):
#     baseArea = baseLength ** 2
#     return height * baseArea / 3
#
#
# ##
# # This program computes the volume of pyramid.
# # and provide a unit test for the function
# #
# def main():
#     print("Volume:", pyramidVolume(9, 10))
#     print("Expected : 300")
#     print("Volume:", pyramidVolume(0, 10))
#     print("Expected : 0")
#
# # start the program
# main()

################## Box string function ##################

# ## Print hyphens above and below the input string
# # @param input string
# # no return value
#
# def boxString(contents):
#     n = len(contents)
#     if n == 0:
#         return
#     print("-" * (n+2))
#     print("!" + contents + "!")
#     print("-" * (n + 2))
#
# boxString("Hello Roops")
# boxString("")
# boxString("Hello Hrish")

################## Parameterized function that prompts user for input ##################

# ## Check if the time entered is valid
# # @param low and high int values that the valid ranges for hours and minutes
# # @return hours, minutes entered
#
# def main() :
#     print("Please enter a time: hours, then minutes.")
#     hours = readIntBetween(0, 23)
#     minutes = readIntBetween(0, 59)
#     print("You entered %d hours and %d minutes." % (hours, minutes))
#
#
# def readIntBetween(low, high) :
#     value = int(input("Enter a value between " + str(low) + " and " +
#     str(high) + ": "))
#     while value < low or value > high :
#         print("Error: value out of range.")
#         value = int(input("Enter a value between " + str(low) + " and " +
#         str(high) + ": "))
#     return value
# # Start the program.
# main()

# ################## Use of multiple functions ##################
# #
# # #
# # # This program returns text equivalent of numbers under 1000.
# # #
# # #
# #
# # def main():
# #     value = int(input("Please enter a positive integer < 1000"))
# #     print(intName(value))
# #
# #
# # def intName(number):
# #     part = number
# #     name = ""
# #
# #     if part >= 100:
# #         name = digitName(part//100) + " hundred"
# #         part = part % 100
# #
# #     if part >= 20:
# #         if len(name) > 0:
# #             name = name + " " + "and"
# #         name = name + " " + tensName(part)
# #         part = part % 10
# #     elif part >= 10:
# #         name = name + " " + teenName(part)
# #         part = 0
# #
# #     if part > 0:
# #         name = name + " " + digitName(part)
# #
# #     return name
# #
# #
# #
# # def digitName(number):
# #     name = ""
# #     if number == 1:
# #         name = "one"
# #     elif number == 2:
# #         name = "two"
# #     elif number == 3:
# #         name = "three"
# #     elif number == 4:
# #         name = "four"
# #     elif number == 5:
# #         name = "five"
# #     elif number == 6:
# #         name = "six"
# #     elif number == 7:
# #         name = "seven"
# #     elif number == 8:
# #         name = "eight"
# #     elif number == 9:
# #         name = "nine"
# #     else:
# #         name = "zero"
# #     return name
# #
# #
# # def teenName(digit):
# #     if digit == 10: name = "ten"
# #     elif digit == 11: name = "eleven"
# #     elif digit == 12:
# #         name = "twelve"
# #     elif digit == 13:
# #         name = "thirteen"
# #     elif digit == 14:
# #         name = "fourteen"
# #     elif digit == 15:
# #         name = "fifteen"
# #     elif digit == 16:
# #         name = "sixteen"
# #     elif digit == 17:
# #         name = "seventeen"
# #     elif digit == 18:
# #         name = "eigteen"
# #     elif digit == 19:
# #         name = "nineteen"
# #     return name
# #
# #
# # def tensName(digit):
# #     if digit >= 90: name = "ninety"
# #     elif digit >= 80: name = "eighty"
# #     elif digit >= 70:
# #         name = "seventy"
# #     elif digit >= 60:
# #         name = "sixty"
# #     elif digit >= 50:
# #         name = "fifty"
# #     elif digit == 15:
# #         name = "fifteen"
# #     elif digit >= 40:
# #         name = "fourty"
# #     elif digit >= 30:
# #         name = "thirty"
# #     elif digit >= 20:
# #         name = "twenty"
# #     return name
# #
# #
# # main()


################## Recursive functions ##################
# def printTriangle(sideLength):
#     if sideLength < 1: return
#     printTriangle(sideLength - 1)
#     print("[]" * sideLength)
#
#
# printTriangle(7)

################## Sum of digits in a number with and without Recursive functions ##################

# Without recursive functions\

# n = 1792
# total = 0
# while n > 0:
#     digit = n % 10
#     total = total + digit
#     n = n // 10
# print(total)

# with recursive funtion

# def digitSum(n):
#     if n == 0:
#         return 0
#     return digitSum(n // 10) + n % 10
#
# sumDig = digitSum(20567)
# print(sumDig)

# def digitsum(n):
#     if n == 0:
#         return 0
#     else:
#         return digitsum(n // 10) + n % 10
#
# num = int(input("Enter an positve integer: "))
# print("Sum of digits is: ",digitsum(num))
#
# ################# Global variable #################
#
# num1 = 3 # Global variable can be used everywhere
#
# def main():
#     print("Test #1")
#     print("My num1 in main is:", num1) # Using my global variables here!
#     test()
#     print("My num1 in main after test is:", num1)
#
# def test():
#     global num1
#     num1 += 2
#     print("My num1 in test is:", num1) # And here!
#
#
# main()
#
# num1 = 3 # Global variable can be used everywhere
#
# def main():
#     print("Test #1")
#     print("My num1 in main is:", num1) # Using my global variables here!
#     test()
#     print("My num1 in main after test is:", num1)
#
# def test():
#     global num1
#     num1 += 2
#     print("My num1 in test is:", num1) # And here!
#
#
# main()


# ################## Lab exercise 1  ##################
# def allTheSame(x, y, z):
#     if x == y and y == z:
#         result = True
#     else:
#         result = False
#     return result
#
# def main():
#     result = allTheSame(17, 20, 13)
#      print("x = 17, y = 20 and z = 13.\n The statement x = y = z in this case is ", True)
#     print("x = 17, y = 20 and z = 13.\n The statement x = y = z in this case is ", allTheSame(17, 20, 13))
#     result = allTheSame(10, 10, 10)
#     print("x = 10, y = 10 and z = 10.\n The statement x = y = z in this case is ", result)
#     result = allTheSame("fox", "fox", "pig")
#     print("x = fox, y = fox and z = pig.\n The statement x = y = z in this case is ", result)
#
# main()

# ################## Lab exercise 2  ##################
# VOWELS = 'aeiou'
# def countVowels(str):
#     vowelcount = 0
#     for char in str:
#         if char.lower() in 'aeiou':
#             vowelcount += 1
#     return vowelcount
#
# def main():
#     print("The count of vowels in the string %s is %d" % ('I love you', 5))
#     print("Program Output: The count of vowels in the string %s is %d" % ('I love you', countVowels('I love you')))
#     print("The count of vowels in the string %s is %d" % ('Fox and cow', 3))
#     print("Program Output: The count of vowels in the string %s is %d" % ('Fox and cow', countVowels('Fox and cow')))
#
# main()