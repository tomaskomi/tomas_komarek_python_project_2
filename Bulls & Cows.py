""""
Projekt_2.py: druhý projekt do Engeto Online Python Akademie")
author: Tomáš Komárek
email: tomaskomi@gmail.com
discord: tomaskomi
"""

import random

separator = "-" * 47

def generate_starting_number():
    """Generates a random four-digit number that doesn't start with zero."""
    while True:
        number = str(random.randint(1000, 9999))
        if number[0] != "0":
            return number

def count_cows(guess, random_number):
    """Counts the number of identical digits, regardless of their index."""
    count = 0
    for number in str(guess):
        if number in str(random_number) and number != random_number[str(guess).index(number)]:
            count += 1
    return count

def count_bulls (guess, random_number):
    """Counts the number of identical digits located at the same index in both arguments"""
    count = 0
    for number_1, number_2 in zip(str(guess), str(random_number)):
        if number_1 == number_2:
            count += 1
    return count

def adjust_word (word, amount):
    """Adjusts the expression to the correct form based on whether it is singular or plural."""
    if amount != 1:
        word += "s"
    return word

random_number = generate_starting_number()
attempts = 0
already_tried = set()


print ("Hi there!")
print(separator)
print ("I've generated a random 4 digit number for you.")
print ("Let's play a bulls and cows game.")
print(separator)


while True:

    guess = input("Enter a number:")
    if len(guess) != 4 or not guess.isdigit() or guess[0] == "0":
        print("Enter a four-digit number that does not start with 0.")
        continue

    if guess in already_tried:
        print("This number was already tried, enter another number.")
        continue

    already_tried.add(guess)
    attempts += 1
    bulls = count_bulls(guess, random_number)
    cows = (count_cows (guess, random_number))


    print (f"{separator}\n>>> {guess} \n {adjust_word("Bull",bulls)} {bulls}, {adjust_word("Cow",cows)} {cows} \n {separator} ")
    if bulls == 4:
        print(f"Congratulations! You guessed the secret number '{random_number}' "
              f"in {attempts} attempts.")
        break








