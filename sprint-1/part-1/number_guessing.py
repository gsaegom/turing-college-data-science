# 1 Numeric types | Exercise 1 ■ Number guessing game
#
# This first exercise introduces a number of topics that will repeat themselves over your Python career: loops,
# user input, converting types, and comparing values.
#
# More specifically, programs all have to get input to do something interesting, and that input often comes from the
# user. Knowing how to ask the user for input not only is useful, but allows us to think about the type of data we’re
# getting, how to convert it into a format we can use, and what the format would be.
#
# As you might know, Python only provides two kinds of loops: for and while. Knowing how to write and use them will
# serve you well throughout your Python career. The fact that nearly every type of data knows how to work inside a
# for loop makes such loops common and useful. If you're working with database records, elements in an XML file,
# or the results from searching for text using regular expressions, you'll be using for loops quite a bit.
#
# For this exercise
#
# Write a function (guessing_game) that takes no arguments. When run, the function chooses a random integer between 0
# and 100 (inclusive). Then ask the user to guess what number has been chosen. Each time the user enters a guess,
# the program indicates one of the following:
# Too high
# Too low
# Just right
# If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
# The program only exits after the user guesses correctly. We’ll
# also be prompting the user to enter text with the input function. We’ll actually be using input quite a bit in this
# book to ask the user to tell us something. The function takes a single string as an argument, which is displayed to
# the user. The function then returns the string containing whatever the user entered; for example:
#
# name = input('Enter your name: ')
# print(f'Hello, {name}!')
import random

if __name__ == '__main__':
    def guessing_game():
        name = input('Enter your name: ')
        print(f'Hello, {name}!')
        number = random.randint(0, 100)
        guess = int(input('Guess a number between 1 and 100'))
        chances = 3
        while number != guess and chances > 0:
            if guess < number:
                chances -= 1
                guess = int(input('Too low! Try again?'))
            if guess > number:
                chances -= 1
                guess = int(input('Too high! Try again?'))
        print(f'Just right! Well done, {name}')


    guessing_game()
