import random
import time
import os

## Car themed hangman game
word_dictionary = [("ford", "American manufacturer. Has a blue logo."),
                   ("ferrari", "Exotic manufacturer. Their cars in red are iconic."),
                   ("rolls royce", "Luxury manufacturer. Top of the line. Currently makes the most expensive car in the world"),
                   ("honda", "Japanese manufacturer. Known to make reliable 'bulletproof' cars."),
                   ("bugatti", "French manufacturer. Known for setting world speed records."),
                   ("ford mustang", "Well known muscle car"),
                   ("nissan gtr", "Japanese sports car revered by enthusiasts. Sometimes referred to as godzilla by tuners."),
                   ("jeep", "American manufacturer, Known for making off-road vehicles for the military."),
                   ("bmw", "German manufacturer. Known for the iconic kidney grilles."),
                   ("vw beetle", "This was a people's car by a brand whose name meant 'people's car'"),
                   ]
stickman_art = ['______\n|\n|\n|\n|___',
                '______\n|    O\n|\n|\n|___',
                '______\n|    O\n|    | \n|\n|___',
                '______\n|    O\n|   /|\n|\n|___',
                '______\n|    O\n|   /|\ \n|\n|___',
                '______\n|    O\n|   /|\ \n|   /\n|___',
                '______\n|    O\n|   /|\ \n|   / \ \n|___']

def blank_generator(list_index):
    blank = ""
    for char in word_dictionary[list_index][0]:
        if char == " ":
            blank = blank + " "
        else:
            blank = blank + "_"
    return blank

# check for presence of other than lowercase letters and space
def guess_validity(guess):
    for char in guess:
        if ord("z") >= ord(char) >= ord("a") and len(guess) == 1:
            valid = True
        else:
            valid = False
            break
    return valid

# display: the variable containing blanks and guessed letters
# guessword = word_dictionary[L_index][1]: guess word of current round
def replace_letter(guess_letter):
    list_display = list(display)
    counter = 0
    for char in guessword:
        if guess_letter == char:
            list_display[counter] = guess_letter
        counter = counter + 1
    new_display = "".join(list_display)
    return new_display

print('''
 __          __  _                          
 \ \        / / | |                         
  \ \  /\  / /__| | ___ ___  _ __ ___   ___ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
    \  /\  /  __/ | (_| (_) | | | | | |  __/
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|''')
print("              to Vehicular Hangman!")
print('''                    _______
                   //  ||\ \ 
             _____//___||_\ \___
             )  _          _    \ 
             |_/ \________/ \___|
            ___\_/________\_/______
''')
print('''
a. There are 5 rounds in this hangman game.
b. You will win the game once you finish all 5 rounds.
c. Each round will consist of a single word from our dictionary, and you will guess
   the word.
d. Each letter that you guess that is NOT in the word, will add a stroke to the little
   guy → see right. The little stick man will have 6 lives. Namely: Head, body,
   left arm, right arm, left leg, right leg.
e. Once the little stick man is entirely “hung”, you will have exhausted your guess
   chances, and it’s game over, you lost.
f. If you guessed the word without the little stick man being hung, you have won the
   round and will move onto the next round.
g. Once you complete all 5 rounds, you are declared a winner.
''')
input("Enter any input to start the game.\n")
print("")

for round in range(5):
    print("\nStarting round ", round+1, "...", sep="")
    life = 0
    incorrect_letters = []
    guessed_letters = []
    randint = random.randint(0, 9)
    guessword = word_dictionary[randint][0]
    display = blank_generator(randint)
    loss = False
    while loss == False:
        print("\n", word_dictionary[randint][1], sep="")
        print(stickman_art[life])
        print("Your guess so far: ", display)
        print("Incorrect letters: ", incorrect_letters)
        print("")
        if life == 6:
            loss = True
        elif display == guessword:
            break
        else:
            while True:
                guess = input("Guess a letter: ")
                # program should accept single letter inputs
                if guess_validity(guess) == False:
                    print("Guess must be a single lowercase letter.\n")
                elif guess in guessed_letters:
                    print("You have already guessed this letter.\n")
                else:
                    break
            if guess in guessword:
                display = replace_letter(guess)
            else:
                incorrect_letters.append(guess)
                life = life + 1
            guessed_letters.append(guess)
    if loss == True:
        print("OOPS, you’ve exhausted your chances. Game over, better luck next time!\n")
        break
    elif round != 4:
        print("Look! You got it! Moving on to the next round...\n")

if loss == False:
    print("Congratulations, you have completed all five rounds and won Vehicular Hangman! Please play again!")
