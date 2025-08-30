# Random
import random

# random.randint(a,b)
random_integer = random.randint(1,10)
print(random_integer)

# random.random() -> 0.0 <= x < 1.0 (you can multiply)
random_number_0_to_10 = random.random() * 10
print(random_number_0_to_10)

# random.uniform(a,b) -> a<= x <= b
random_float = random.uniform(1, 10)
print(random_float)

# list
states_of_america = ["Delaware", "Pennsylvania", "..."]
print(states_of_america[0])
print(states_of_america[-1])
states_of_america[2] = "New Jsersey"
print(states_of_america[2]) 
states_of_america.append("Georgia")
print(states_of_america)
states_of_america.extend(["Newyork", "Washington"])
print(states_of_america)

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends[random.randint(0, 4)])
print(random.choice(friends))

# Lists in List
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "PEaches", "cherries", "Pear"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Day4 Project: Randomisation and Python Lists
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: "))
computer = random.randint(0,2)
if (computer - user == -1) or (computer - user == 2):
    print("You win.")
elif computer - user == 0:
    print("Draw")
elif (computer - user == -2) or (computer - user ==1):
    print("You lose.")
else:
    print("Did you choose correctly?")