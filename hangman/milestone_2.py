#import random
import random

#create a list of 5 fav. fruits and print the list
word_list = ["grapes", "strawberry", "orange", "mango", "kiwi"]
print(word_list)

#use random module which returns a random item from given sequence
word = random.choice(word_list)
print(word)

#take an user input which returns user input in the form of string
guess = input("Enter a single letter ")

#check that the input is single character
if len(guess) == 1 and guess.isalpha() :
    print("Good guess!")
else :
    print("Oops! That is not a valid input.")



