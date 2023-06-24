# coding rooms (updated): https://app.codingrooms.com/w/c8uPB3XQWHl8
# unscramble words game. theme: automobile manufacturers
import random, os

def clearConsole(): # function to clear console. Doesnt work in pycharm but should work in coding rooms
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

print("Scrambled Words Game: Car Brands\n",
'''
instructions:
The theme of this Scrambled Words game is car brands. The player will attempt to enter the unscrambled names of various automobile manufacturers. 
The game will consist of 5 rounds. In each round, the player will have 3 attempts to unscramble the word. Letter case does not matter, however hyphens and spaces do. 
Points will be deducted for every incorrect attempt. Good luck! 
'''
)
input("Press enter to begin the game.")

words_list = ["Honda", "Toyota", "Mazda", "Nissan", "BMW", "Mercedes-Benz", "Audi", "Ford", "Lamborghini", "Ferrari", "Aston Martin"]

points = 15 # total number of tries. every time user gets a word wrong, one try is subtracted from the total. The score will be printed out as a percentage in the end.
correct_guesses = 0 # total number of words the user guessed correctly.

for round_num in range(1,6): # 5 rounds with a different word each round
    clearConsole()

    word = random.choice(words_list) # choose this round's word

    # to scramble the word:
    scrambled_word = list(word)
    random.shuffle(scrambled_word)
    scrambled_word = "".join(scrambled_word)

    print("\nRound ", round_num, "\n", scrambled_word, "\n", sep="")

    for attempt in range(1,4):
        guess = input("Unscramble the word: ").lower().strip()
        if guess == word.lower():
            correct_guesses += 1
            print(f"'{guess}' is correct!\n")
            break
        else:
            points -= 1
            print(f"'{guess}' is incorrect! \nRemaining attempts this round: ", 3-attempt, "\n")


final_score = round(points/15*100)
print("You got ", correct_guesses, " out of 5 words correct! \nFinal score: ", final_score, "%", sep="")


# notes:
# maybe add quit option
# maybe try to wipe console for cleaner print out
# maybe format headers and centered text or something