# Subscripting 
print("Hello"[4]) # o
print("Hello"[-1]) # o
print("Hello"[0]) # H

# String
print("123" + "456")

# Integer = Whole number
print(123 + 345) # 468

# Large Integers
print(123_456_789) # Python will ignore the "_"

# Float = Floating Point number
print(3.14159)

# Boolean
print(True) 
print(False)

# How to know what type it is?
print(type(123))
print(type(False))
print(type("Hello"))
print(type(123.123))

# Convert the data type
type(int("123"))
print((bool(0)))
print((bool(1)))
print(int(2.6)) # 2 (round down)

print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# Calculate
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3) # float
print(7 // 2) # round down
print(2 ** 3) # Exponents 2^3
print(round(3.555, 2)) # round

# User scores a point
score = 0
score += 1
score += 1
print(score)

# f-string
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

# Day2 Project: Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
print("Each person should pay: $" + str(round(bill*(1 + tip / 100)/people, 2)))