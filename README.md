# Project Documentation

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

- In this Project first, set up a github account to track changes to our code and save them online in a GitHub repo.

## Milestone 2

### Task 1:
- Created a file named milestone_2.py. In Python, Lists are used to store multiple data in a single variable. 
- In this task, we are going to create a list of words containing the names of 5 favourite fruits and will assign this list to a variable called word_list.

```python

    word_list = ["grapes", "strawberry", "orange", "mango", "kiwi"]
    print(word_list)

```

### Task 2:
- Use the 'random' module which is one of Python's built-in modules. It has a choice method which returns a random item from a given sequence. 
- To import a module, used the import keyword and create the random.choice() method and pass the word_list variable into the choice method and assigned it to the variable called word.

```python

    import random 
    word = random.choice(word_list)
    print(word)

```

### Task 3:
- Python has an input() function that takes input from the screen. Use the input function to ask the user to enter a single letter and assigned it to the guess.

```python

    guess = input("Enter a single letter ")

```

### Task 4:
- Check that the input is a single character.
- Create an if statement that checks if the length of the input is equal to 1 and the input is an alphabet and in the if statement, print a message that says "Good guess!".
- Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.

```python

    if len(guess) == 1 and guess.isalpha() :
        print("Good guess!")
    else :
        print("Oops! That is not a valid input.")

```

## Milestone 3:

### Task 1:
- Create a file name milestone_2.py, create a while loop and set the condition to True and within the loop asked the user to guess a letter and assign the letter to a variable guess.
- Check the guess is a single, alphabetical character.
- If the guess passes the checks, break out of the loop. If the guess does not pass the checks, then print a message "Invalid letter please, enter a single alphabetical character."

### Task 2:
- Create an if statement that checks if the guess is in the word.
- In the body of the if statement, print a message using the formatted string "Good guess! {guess} is in the word.".
- Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.

```python

    while True:
        guess = input("enter a single letter")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
```

### Task 3:
- Create 2 functions, check_guess and ask_for_input which contain the code for those two things.
The check_guess function will take the guessed letter as an argument and check if the letter is in the word.
- Define a function called check_guess. pass in the guess as a parameter for the function. 
- Within the body of the function 
  - Convert the guess into lower case.
  - Code to check if the guess is in the word into this function block.
- Define a function called ask_for_input.
 - code to check if the input is a valid guess task into this function block.
 - Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.
- Outside the function, call the ask_for_input function to test your code.

```python

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
```

## Milestone 4:

### Task 1:
-  Create a new script called milestone_4.py. This file will contain the code for the third milestone.
- Create a class called Hangman.
- Inside the class, create an __init__ method to initialise the attributes of the class. Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.
- Initialise the following attributes:
 - word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.
 - word_guessed: list - A list of the letters of the word, with '' for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].
 - num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
 - num_lives: int - The number of lives the player has at the start of the game.
 - word_list: list - A list of words.
 - list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.

### Task 2:
- create the check_guess method.
- Define a method called check_guess. Pass the guess to the method as a parameter. In the body of the method, write the code for the following steps:
 - Convert the guessed letter to lower case
 - Create an if statement that checks if the guess is in the word
 - In the body of the if statement, print a message saying "Good guess! {guess} is in the word.
- define a method called ask_for_input. In the body of the method, do the following
 - Create a while loop and set the condition to True.
 - Ask the user to guess a letter and assign this to a variable called guess.
 - Create an if statement that runs if the guess is NOT a single alphabetical character.
 - In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
 - Create an elif statement that checks if the guess is already in the list_of_guesses.
 - In the body of the elif statement, print a message saying "You already tried that letter!".
- f the guess is a single alphabetical character and it's not already in the list_of_guesses:
 - Create an else block and call the check_guess method. Remember to pass the guess as an argument to this method.
 - Add the guess to the `list_of_guesses.
- Call the ask_for_input method to test your code.

### Task 3:
- In the if block of the check_guess method, after print statement, do the following:
 - Create a for-loop that will loop through each letter in the word.
 - Within the for-loop, do the following:
  - Create an if statement that checks if the letter is equal to the guess.
  - In the if block, replace the corresponding "_" in the word_guessed with the guess. HINT: You can index the word_guessed at the position of the letter and assign it to the letter.
- Outside the for-loop, reduce the variable num_letters by 1.

### Task 4:
- In the check_guess method, Create an else statement.
- Within the else block:
 - Reduce `num_lives' by 1.
 - print a message saying "Sorry, {letter} is not in the word."
 - print another message saying "You have {num_lives} lives left."
- Lastly, append the guess to the list_of_guesses. Ensure you do this outside the else block so that the letter can be appended to the list_of_guesses in both conditions.

```python

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

```

## Milestone 5:

### Task 1:
-  Create a function called play_game that takes no arguments. Inside the function, write the code for the following steps:
 - Create a list of your 5 favorite fruits and assign this to a variable called word_list.
 - Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game.
 - Pass the word_list and num_lives as arguments to the game object.
 - Create a while loop and set the condition to True. In the body of the loop, do the following:
  - Check if the num_lives is 0. If it is, that means the game has ended and the user lost. Print a message saying 'you lost!'.
  - Next, check if the num_letters is greater than 0. In this case, you would want to continue the game, so you need to call the ask_for_input method.
  - If the num_lives is not 0 and the num_letters is not greater than 0, that means the user has won the game. Print a message congratulating the user for winning the game.
- Outside the function, call your play_game function to play your game.

```python 

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

```