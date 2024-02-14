# My Final Project! This program can solve wordles, anagrams, the New York Times Spelling Bee, and provide a
# list of words that can be made with given letters.
# Author: Cooper Zion

import random
import string

from colorama import Fore

# Get my word lists from files
with open('word_list_3', 'r') as f:
    word_list_3 = []
    for line in f:
        word_add = line
        word_add = word_add.rstrip('\n')
        word_list_3 += [word_add]

    word_list_3.sort()

with open('word_list_4', 'r') as f:
    word_list_4 = []
    for line in f:
        word_add = line
        word_add = word_add.rstrip('\n')
        word_list_4 += [word_add]

    word_list_4.sort()

with open('word_list_5', 'r') as f:
    word_list_5 = []
    for line in f:
        word_add = line
        word_add = word_add.rstrip('\n')
        word_list_5 += [word_add]

    word_list_5.sort()

with open('word_list_6', 'r') as f:
    word_list_6 = []
    for line in f:
        word_add = line
        word_add = word_add.rstrip('\n')
        word_list_6 += [word_add]

    word_list_6.sort()

with open('word_list_7', 'r') as f:
    word_list_7 = []
    for line in f:
        word_add = line
        word_add = word_add.rstrip('\n')
        word_list_7 += [word_add]

    word_list_7.sort()

with open('NYT_words', 'r') as f:
    word_list_NYT = []
    for line in f:
        word_add = line
        word_add = word_add.lower()
        word_add = word_add.rstrip('\n')
        word_list_NYT += [word_add]

    word_list_NYT.sort()

# Make one large word list with ALL the words for the spelling bee and word list constructor
total_word_list = word_list_3 + word_list_4 + word_list_5 + word_list_6 + word_list_7
for word in word_list_NYT:
    if len(word) > 7:
        total_word_list.append(word)


def wordle():
    """Solve wordles with input for correct, present, and absent letters. Output a list of possible words"""
    run_input = True
    while run_input:
        try:
            # Provide the definitions for each color
            print(Fore.GREEN + '\nCorrect letters', Fore.WHITE + 'are the green letters that have confirmed positions.')
            print(Fore.LIGHTYELLOW_EX + 'Present letters', Fore.WHITE + 'are the yellow letters that are in the word '
                                                                        'but in a different spot.')
            print(Fore.RED + 'Absent letters', Fore.WHITE + 'are gray letters that are not in the word.')

            # Collect the most recent guess
            guess = str(input('\nEnter your last guess: '))

            # Collect the color of each letter in the guess
            print('Now enter the color of the letter in each space.')
            print('Type', Fore.GREEN + "C", Fore.WHITE + 'for', Fore.GREEN + 'correct letters.')
            print(Fore.WHITE + 'Type', Fore.LIGHTYELLOW_EX + "P", Fore.WHITE + 'for', Fore.LIGHTYELLOW_EX +
                  'present letters.')
            print(Fore.WHITE + 'Type', Fore.RED + "A", Fore.WHITE + 'for', Fore.RED + 'absent letters.')
            status = str(input(Fore.WHITE + 'Enter them separated by only a comma (ie. a,b,c,d): '))

            status_list = status.split(',')

            # Collect the other absent letters
            print('If there are any other', Fore.RED + 'absent', Fore.WHITE + 'letters,')
            absent_letters = str(input('enter them here separated by only a comma (ie. a,b,c,d): '))

            run_input = False

        except Exception:
            print('Invalid Input!')

        guess = guess.lower()
        status = status.upper()

        absent_list = absent_letters.split(',')

        new_word_list = []

        print("Solving...")

        for word in word_list_5:
            new_word_list.append(word)

        for word in word_list_5:
            i = 0
            while i < 5:
                if status_list[i] == 'C' and guess[i] != word[i]:
                    if word in new_word_list:
                        new_word_list.remove(word)

                if status_list[i] == 'A' and guess[i] in word:
                    if word in new_word_list:
                        new_word_list.remove(word)

                if status_list[i] == 'P' and guess[i] == word[i]:
                    if word in new_word_list:
                        new_word_list.remove(word)

                if status_list[i] == 'P' and guess[i] not in word:
                    if word in new_word_list:
                        new_word_list.remove(word)

                for item in absent_list:
                    if item in word and word in new_word_list:
                        new_word_list.remove(word)

                i += 1

    print('Possible answers are:')
    for guess in new_word_list:
        print(f'{guess}')


def anagram():
    """Unscramble an anagram"""
    run_input = True
    while run_input:
        try:
            in_word = str(input('Enter a word between 3 and 7 letters you want to unscramble: '))
            if len(in_word) > 7:
                print(f'"{in_word}" is too long to unscramble, please enter a word with 7 or fewer letters.')
            elif len(in_word) < 3:
                print(f'"{in_word}" is too short to unscramble, please enter a word with 3 or more letters.')
            else:
                run_input = False
                print(in_word)
                print('Solving...')
        except Exception:
            print('Invalid Input!')

    word = in_word.lower()

    while word not in total_word_list:
        new_word = random.sample(word, len(word))
        word = ""
        i = 0
        while i < len(new_word):
            word += new_word[i]
            i += 1

    print(f'{in_word} is an anagram for {word}!')


def spelling_bee():
    """Generate a list of words that solve the daily NYT spelling bee"""
    outer_letters = str(input('Enter the outer ring of letters separated by only a comma (ie. a,b,c,d): '))
    required_letter = str(input('Enter the required letter in the center: '))
    print('Solving...')

    outer_letters_list = outer_letters.split(',')
    letters_list = outer_letters_list + [required_letter]

    non_letters_list = list(string.ascii_lowercase)
    for item in letters_list:
        non_letters_list.remove(item)

    answer_words = []
    pangram_list = []
    for word in word_list_NYT:
        answer_words.append(word)

    for word in word_list_NYT:
        for item in non_letters_list:
            if item in word and word in answer_words:
                answer_words.remove(word)
        if required_letter not in word and word in answer_words:
            answer_words.remove(word)
        if len(word) < 4 and word in answer_words:
            answer_words.remove(word)
        count = 0
        for item in letters_list:
            if item in word:
                count += 1
        if count == 7:
            pangram_list.append(word)

    print('The answers are...')
    for item in answer_words:
        print(item)
    print('The pangram(s) is/are...')
    for item in pangram_list:
        print(item)


def word_lists():
    """Generate a list of words that can be made with an input of letters"""
    letters = str(input('Enter a list of letters to make words with separated by a comma (ie. a,b,c,d): '))
    letters_list = letters.split(',')

    non_letters_list = list(string.ascii_lowercase)
    for item in letters_list:
        non_letters_list.remove(item)

    answer_words = []
    for word in total_word_list:
        answer_words.append(word)

    for word in total_word_list:
        for item in non_letters_list:
            if item in word and word in answer_words:
                answer_words.remove(word)

    print('The list of words that can be made with these letters are...')
    for item in answer_words:
        print(item)


def main():
    print('Welcome to the Cure for Bewilderment!')
    opt_var = True
    while opt_var != 5:
        opt_var = int(input('1: Solve a Wordle\n'
                            '2: Solve an Anagram\n'
                            '3: Solve the Spelling Bee game from the New York Times\n'
                            '4: Generate a list of words from possible letters\n'
                            '5: Quit\n'
                            'What would you like to do? Type the number that corresponds with your choice. '))

        while opt_var != 1 and opt_var != 2 and opt_var != 3 and opt_var != 4 and opt_var != 5:
            opt_var = str(input('Please select a valid option. '))

        if opt_var == 1:
            wordle()
        elif opt_var == 2:
            anagram()
        elif opt_var == 3:
            spelling_bee()
        elif opt_var == 4:
            word_lists()
        else:
            pass

        # Separate games from one another
        print('\n' * 2)


main()
