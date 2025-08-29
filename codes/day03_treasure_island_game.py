# Condition
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120: # equal to is == not =
    print("You can ride the rollercoaster.")
    age = int (input("What is your age?: "))
    if 18 < age:
        bill = 12
        print("Adult tickets are $12")
    elif 12 <= age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 5
        print("Child tickets are $5.") 
    
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.: ")
    if wants_photo == "y":
        bill += 3 # bill = bill + 3
    print(f"Your final bill is {bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")

# you can have remainder by using %
print(10 % 3)

number = int(input("Number: "))
if number % 2 == 0:
    print("It's an even number.")
else:
    print("It's an odd number.")

# Pizza Price Calculator
# Samll: $15, Medium: $20, Lager: $25
# Add pepperoni for small pizza: +$2
# Add pepperoni for medium or large pizza: +$3
# Add extra cheese for any size pizza: +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you wants? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill +=1
print(f"Your final bill is {bill}.")

# Day3 Project: Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************         
      ''')
print("Welcome to Treasure Island. Your mission is to find the treasure.")
answer = input("You got to the cross road. Do you want to go to left or right?: ")
if answer == "left":
    answer = input("You found nothing. Do you want to wait for the boad or swim?\nWrite wait or swim: ")
    if answer == "wait":
        answer = input("You landed the other island.\nYou found three doors.\nWhich door do you want to open?\nType blue, yellow or red: ")
        if answer == "yellow":
            print("Congratulations! You found the treasure!")
        else:
            print("You woke up the bear and you died.")
    else:
        print("You met a shark and you died.")
else:
    print("You met a tiger and you died.")