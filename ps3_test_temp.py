#Problem 1:
import random
import string
#
#     """
#     Returns the score for a word. Assumes the word is a
#     valid word.
# 
# 	The score for a word is the sum of the points for letters
# 	in the word multiplied by the length of the word, plus 50
# 	points if all n letters are used on the first go.
# 
# 	Letters are scored as in Scrabble; A is worth 1, B is
# 	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
# 
#     word: string (lowercase letters)
#     returns: int >= 0
#     """
# 	
# def get_word_score(word):
# 	SCRABBLE_LETTER_VALUES = {
# 		'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
# 	}
# 	letter_list = []
# 	score = 0
# 	number_of_letters = 0
# 	for x in word:
# 		letter_list = letter_list + [x,]
# 		number_of_letters = number_of_letters + 1
# 	if number_of_letters == 7:
# 		for y in letter_list:
# 			score = score + SCRABBLE_LETTER_VALUES[y]
# 		score = score * number_of_letters
# 		score = score + 50
# 	else:
# 		for y in letter_list:
# 			score = score + SCRABBLE_LETTER_VALUES[y]
# 		score = score * number_of_letters
# 		
# 	return score
# 
# my_word = raw_input("Please enter a word: ")
# #number = 5
# 
# print 'The word is: ', get_word_score(my_word)
# 
# #________________________________________________________________________________

# Problem 2:
# 
#     """
#     Returns a random hand containing n lowercase letters.
#     At least n/3 the letters in the hand should be VOWELS.
# 
#     Hands are represented as dictionaries. The keys are
#     letters and the values are the number of times the
#     particular letter is repeated in that hand.
# 
#     n: int >= 0
#     returns: dictionary (string -> int)
#     """

def deal_hand(n):

    hand={}
    num_vowels = n / 3
    VOWELS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

# readable_letter_list = ' '
# letter_dict = deal_hand(7)
# for i in range(len(letter_dict)):
# 	readable_letter_list = readable_letter_list + str(letter_dict[i])

hand = deal_hand(7)
keys = list(hand.keys())
print keys
print "Your letters are: " + str(hand)
