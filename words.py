

def print_upper_words(words):
 """this works by taking an array of words and iterating through every word in the array
The words in the array are converted to uppercase with the upper() and printed
during every interation
"""
 for word in words:
    print(word.upper())

def print_words_e(words):
   

 for word in words:
   if(word[0] == 'e' or word[0]== 'E'):
     print(word.upper())





def print_upper_words_list(words, must_start_with):
 """this works by taking an array of words and iterating through every word in the array
The words in the array are converted to uppercase with the upper() and printed
during every interation.  In every iteration of word an iteration of letter is run
if the first letter of the word and the letter in must start with are equal,
the word is printed in uppper case
"""
 for word in words:
    for letter in must_start_with:
        if(word[0]==letter):
            print(word.upper()) 