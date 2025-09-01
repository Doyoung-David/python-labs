# Hang_man
import random
stages = [
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = ""
for k in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    user_word = input("Guess the letter.: ").lower()
    display = ""
    for i in chosen_word:
        if user_word == i:
            print("Right")
            display += i
            correct_letters.append(i) 
        elif i in correct_letters:
            display += i
        else:
            display += "_"
    print(display)
    if user_word not in chosen_word:
        lives -= 1
        if lives == 0:
         game_over = True
         print("You lose.") 

    if "_" not in display:
        game_over = True
        print("You win.")
    print(stages[lives])    