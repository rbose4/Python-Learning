# My first python program
print("Hello World")

print("My favourite song is We will rock you")
print("My favourite movie is Sound of Music")
print("My favourite day for the year is November", 18)
print()
print("Hello")
print("World!")

print("Hello World")
print()
print('Good to see you')
print("My favorite numbers are",10+5,"and",3+6)
print("Good morning","'Roopa!'",sep='')
print('G','F','H',sep=',')
print('G','F','H',sep='')
print('09','12','2016',sep=',')
print('roopbose9','gmail',sep='@',end='.')
print('com')

print('Hello')
print('WOrld')

print('roopbose9','gmail',sep='@',end='78')
print('bose')

##
# Lab excercise 2
#

integer1 = int(input("Please enter the first number:"))
integer2 = int(input("Please enter the second number:"))

sum = integer1 + integer2
product = integer1 * integer2
distance = abs(integer1 - integer2)
average_num = sum/2
maxvalue = max(integer1, integer2)

print("%-10s %-3d" % ("Sum:", sum))
print("%-10s %-3d" % ("Product:", product))
print("%-10s %-3d" % ("Distance:", distance))
print("%-10s %-3d" % ("Average:", average_num))
print("%-10s %-3d" % ("Maximum:", maxvalue))
