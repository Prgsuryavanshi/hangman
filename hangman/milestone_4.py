#Task 1:
import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word)* ["_"]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
#Task 2:
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            self.num_letters -= 1
            #Task 3:
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            print("".join(self.word_guessed))
        #Task 4:    
        else: 
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.") 
            #end of task 4:
        self.list_of_guesses += guess           
            #End of Task 3:

    def ask_for_input(self):
        
        guess = input("Guess and enter a single letter - ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)

def play_game():
    word_list = ["grapes", "strawberry", "orange", "mango", "kiwi"]
    number_lives = 5
    game = Hangman(word_list, num_lives=number_lives)

    while True:
        while True:       
            if game.num_lives == 0:
                print(f"You lost! The corect word is '{game.word}' ")
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print("Congratulation you have own the game.")
                break
        replay = input('Do you want to play again(y/n)?')
    
        if replay == 'y':
            game = Hangman(word_list, num_lives=number_lives)
        else:
            break

play_game()






