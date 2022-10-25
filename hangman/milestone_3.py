#Create a while loop and set the condition to True
import random
word_list = ["grapes", "strawberry", "orange", "mango", "kiwi"]
word = random.choice(word_list)

"""
while True:
    guess = input("enter a single letter")
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character.")
    elif guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
"""

#Task 3:
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input("enter a single letter")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")    
    check_guess(guess)

ask_for_input()