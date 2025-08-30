# Loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
print(fruits) # Carried after the Loop done

# Sum and Max
students_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78]
print(sum(students_scores))
print(max(students_scores))

# How to make max myself
standard = 0
for score in students_scores:
    if score > standard:
        standard = score
print(standard)

# range
for number in range(1, 10):
    print(number)

for number in range(1, 11):
    print(number)

for number in range(1, 11, 3):
    print(number)

print(sum(range(1, 101)))

# FizzBuzz Game
for i in range(1, 101):
    if (i % 3 == 0) and (not i % 5 == 0):
        print("Fizz")
    elif (i % 5 == 0) and (not i % 3 == 0):
        print("Buzz")
    elif (i % 5 == 0) and (i % 3 == 0):
        print("FizzBuzz")
    else:
        print(i)

# Day5 Project: Python Loops
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_ing = []
symbols_ing = []
numbers_ing = []
for i in range(1, nr_letters+1):
    letters_ing.append(random.choice(letters))
for i in range(1, nr_symbols+1):
    symbols_ing.append(random.choice(symbols))
for i in range(1, nr_numbers+1):
    numbers_ing.append(random.choice(numbers))
all_ing = letters_ing + symbols_ing + numbers_ing
random.shuffle(all_ing)
result = ''.join(all_ing)
print(result)