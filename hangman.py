import random
from words import words
# from words => It is the file name
# import words => It is the list name
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
# We cannot guess a word if it contains - or ' ' , so we select a word which does not have it.
# We change it to upper to make correct comparisions

def hangman():
    word = get_valid_word(words) # Random word choosed by computer
    word_letters = set(word) # It has all alphabets of the word that computer randomly choose
    alphabet = set(string.ascii_uppercase) # All uppercase letters in English language
    used_letters = set() # What letters the user have guessed

    lives = 6 # Total life

    # We repeat the process untill word is correctly guessed
    while len(word_letters) > 0 and lives > 0:
        # print used letters
        # ' '.join(['a','b','cd']) --> 'a b cd'
        print('You have',lives,' lives left and you have used these letters: ',' '.join(used_letters))

        # Tell the current word
        # Put letters if they are correct
        # Put - where the letters need to be guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() # Get user input

        # We add the letter if it is not in the set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # If the user correctly guessed the letter, remove the guessed letter from the word_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            # If the user did not guess correctly, decrease life by one
            else:
                lives = lives - 1
                print('Letter not in word.')
        elif user_letter in used_letters:
            print('You have already used that character. Please try again!')
        else:
            print('Invalid character. Please try again!')
    # Gets here when len(word_letters) == 0 OR when lives == 0
    if(lives == 0):
        print(f'You died. The word was {word}.')
    else:
        print(f'Yay!! You guessed the word {word} !!!')

hangman()


