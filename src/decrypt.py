#!/usr/bin/python

import sys
from spellchecker import SpellChecker
from itertools import permutations 
  
def allPermutations(str): 
       
    spell = SpellChecker()

    # Get permutations
    permList = permutations(str) 

    jumbledwords = []
    for perm in list(permList): 

        jumbledwords.append(''.join(perm))

    misspelled = spell.unknown(jumbledwords)
    wellspelled = []

    print("Please wait while we compute and show the final suggestions")
    for word in misspelled:

        # Get the one `most likely` answer
        
        correction = spell.correction(word)
        
        # Ensure length of the word is same as search key word
        if len(word) == len(correction):

            # If suggestion is in the list of permutations
            if correction in jumbledwords:

                # Temporary print to have the user glued on
                print(correction)

                # If not repeated
                if correction not in wellspelled:
                    wellspelled.append(correction)


    # Print all suggestions
    print("\n\nFinal Suggestions!")
    for item in wellspelled:
        print(item)



if __name__ == "__main__": 
    allPermutations(sys.argv[1]) 