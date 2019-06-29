# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guess = True
    
    # check every letter in secret word in letters_guessed
    #if a letter from secret word is not found in list
    # returns false else true
    for letter in secret_word:
        if(letter not in letters_guessed):
            guess = False
        
    return guess



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    return_s = ""
    for letter in secret_word:
        if(letter not in letters_guessed):
            return_s += "_ "
        else:
            return_s += letter
    return return_s

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    s = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
             s += letter   
    return s
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")    
    print("-------------")
    print("You have", warnings_left, "warnings left.")
    
    
    while True:
        print("You have", guesses_left, "guesses left.")
        available_letters = get_available_letters( letters_guessed )
        print("Available letters: " + available_letters, end="")
    
        letter_guessed = input("Please guess a letter: ").lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        if letter_guessed.isalpha():
            if(letter_guessed not in letters_guessed):
                letters_guessed.append(letter_guessed)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
            
                if(letter_guessed in secret_word):
                    print("Good guess:", guessed_word)
                else:
                    if letter_guessed in "aeiou":
                        guesses_left -= 2
                    else:
                        guesses_left -= 1
                    print("Oops! That letter is not in my word:", guessed_word)
            else:
                if warnings_left > 0:
                    warnings_left -= 1
                    print("Oops! You've already guessed that letter. You have", warnings_left, "warnings left: {}".format(guessed_word))
                else:
                    guesses_left -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {}".format(guessed_word))
                
        else:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings left: {}".format(guessed_word))
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: {}".format(guessed_word))
                
        print("-------------")
        
        if is_word_guessed( secret_word, letters_guessed):
            unique_letters = []
           
            for char in secret_word:
                if char not in unique_letters:
                    unique_letters.append(char)
            
            print("Congratulations, you won!")
            print("Your total score for this game is:", guesses_left * len(unique_letters))       
            break
            
        if (guesses_left <= 0):
            print("Sorry, you run out of guesses. The word was " + str(secret_word))
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)



# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_without_spaces = ""
    letter_guessed =[]
    for char in my_word:
        if char != ' ':
            my_word_without_spaces += char
        
        if char.isalpha():
            letter_guessed.append(char)
    
    if len(my_word_without_spaces.strip() ) != len(other_word.strip() ):
        return False
    
    for i in range(len(my_word_without_spaces)):
        current_letter = my_word_without_spaces[i]
        other_letter = other_word[i]
        if current_letter.isalpha():
            has_same_letter = ( current_letter == other_letter )
            if not has_same_letter:
                return False
        else:
            if current_letter== "_" and other_letter in letter_guessed:
                return False
        
    return True
   



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words.append(word)
    
    if len(matched_words) > 0:
        for word in matched_words:    
            print(word, end=" ")
        print()
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings_left = 3
    letters_guessed = []
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")    
    print("-------------")
    print("You have", warnings_left, "warnings left.")
    
    
    while True:
        print("You have", guesses_left, "guesses left.")
        available_letters = get_available_letters( letters_guessed )
        print("Available letters: " + available_letters, end="")
    
        letter_guessed = input("Please guess a letter: ").lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        if letter_guessed.isalpha():
            if(letter_guessed not in letters_guessed):
                letters_guessed.append(letter_guessed)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
            
                if(letter_guessed in secret_word):
                    print("Good guess:", guessed_word)
                else:
                    if letter_guessed in "aeiou":
                        guesses_left -= 2
                    else:
                        guesses_left -= 1
                    print("Oops! That letter is not in my word:", guessed_word)
            else:
                if warnings_left > 0:
                    warnings_left -= 1
                    print("Oops! You've already guessed that letter. You have", warnings_left, "warnings left: {}".format(guessed_word))
                else:
                    guesses_left -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {}".format(guessed_word))
       
        elif letter_guessed == "*":
            print("Possible word matches are: ")
            show_possible_matches(guessed_word)
        
        else:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings left: {}".format(guessed_word))
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: {}".format(guessed_word))
                
        print("-------------")
        
        if is_word_guessed( secret_word, letters_guessed):
            unique_letters = []
           
            for char in secret_word:
                if char not in unique_letters:
                    unique_letters.append(char)
            
            print("Congratulations, you won!")
            print("Your total score for this game is:", guesses_left * len(unique_letters))       
            break
            
        if (guesses_left <= 0):
            print("Sorry, you run out of guesses. The word was " + str(secret_word))
            break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
