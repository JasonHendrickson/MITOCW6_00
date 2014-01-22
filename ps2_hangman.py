# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
#    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
#    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

selected_word = choose_word(wordlist)
word_secret = ()
word_display = []

for i in selected_word:
	word_secret = word_secret + (i,)

for i in range(0, len(selected_word)):
	word_display = word_display + ['-']

#print word_display

print 'This is a game of hangman.'
print 'I am thinking of a word ' + str(len(selected_word)) + ' letters long'



max_wrong_guesses = 10
undetermined_letters = len(word_display)
init_undetermined_letters = undetermined_letters
choices_remaining = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


while (undetermined_letters > 0 and max_wrong_guesses > 0):				#while there are undiscovered letters in word_display
	undetermined_letters = len(word_display)							#Und_let must be reset to max before each round commences
	letters_available = ' '

	for r in choices_remaining:
		letters_available = letters_available + r
	print 'Please choose from the following letters: ' + letters_available
	guessed_letter = raw_input('Guess a letter: ')
	print 'You guessed: "' + guessed_letter +'"'

	for n in range(0, len(selected_word)):								#searches word to find guessed letter, replaces if true
		if guessed_letter == word_secret[n]:
			word_display[n] = guessed_letter

	for x in range(0, len(word_display)):						#determines number of undetermined letters
		if word_display[x] != '-':								#if the element at index x is not '-' then there is one fewer  
			undetermined_letters = undetermined_letters - 1		#Decrements until all letters are found

	if undetermined_letters != init_undetermined_letters:		
		init_undetermined_letters = undetermined_letters
		print 'You guessed correctly!'
	else:
		max_wrong_guesses = max_wrong_guesses - 1
		if max_wrong_guesses == 1:
			print "Wrong move, sucka', you only have " + str(max_wrong_guesses) + ' bad choice left!'
		else:
			print "Wrong move, sucka', you only have " + str(max_wrong_guesses) + ' bad choices left!'

	for y in range (0, len(choices_remaining)):
		if guessed_letter == choices_remaining[y]:
			choices_remaining[y] = '-'
	readable_word = ''

	for t in word_display:
		readable_word = readable_word + t
	print "Here's your current word: " + readable_word		

if max_wrong_guesses == 0:
	print "Wah, wah, too many wrong guesses.   You lose!"
	print "The answer was: " + str(selected_word)
else:
	print "Congratulations! You've solved the puzzle!"







