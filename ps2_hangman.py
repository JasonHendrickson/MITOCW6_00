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
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
#print choose_word(wordlist)			#early test of existing code

selected_word = choose_word(wordlist)

print 'This is a game of hangman.'
print 'I am thinking of a word ' + str(len(selected_word)) + ' letters long'
print selected_word					#Ensures that selected_word is returning a reliable result
#word_secret = (selected_word)
#print word_secret
#print word_secret[2]
print selected_word[2]
word_secret = ()
word_display = []
for i in selected_word:
	word_secret = word_secret + (i,)
for i in range(0, len(selected_word)):
	#print i
	word_display = word_display + ['-']
print word_display
print word_secret
for i in range(0,26):
	guessed_letter = raw_input('Guess a letter: ')
	print 'You guessed: "' + guessed_letter +'"'
	for n in range(0, len(selected_word)):
		#print n
		#print word_secret[n]
		if guessed_letter == word_secret[n]:
			word_display[n] = guessed_letter
	print "This is the current state: " + str(word_display)		
	break
	









