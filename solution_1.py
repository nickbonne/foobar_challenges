#!/usr/bin/env python 

'''

Letter format:

         spaces
letter = 1 4
         2 5
         3 6 

Each numbered space has a bump or not.

1 will signify the bump
0 will be flat

'''

b_alpha = [
          ['a', '100000'], ['b', '110000'], 
          ['c', '100100'], ['d', '100110'], 
          ['e', '100010'], ['f', '110100'], 
          ['g', '110110'], ['h', '110010'], 
          ['i', '010100'], ['j', '010110'], 
          ['k', '101000'], ['l', '111000'], 
          ['m', '101100'], ['n', '101110'], 
          ['o', '101010'], ['p', '111100'], 
          ['q', '111110'], ['r', '111010'], 
          ['s', '011100'], ['t', '011110'], 
          ['u', '101001'], ['v', '111001'], 
          ['w', '010111'], ['x', '101101'], 
          ['y', '101111'], ['z', '101011'], 
          ]

# If letter is capitalized, add this string before letter
capital = '000001' 

def answer(text):

    translation = ''

    string_chars = list(text)

    for letter in string_chars:

        if letter == ' ':
            # if letter is actually a space
            translation += '000000'

        for braille_letter in b_alpha:

            if braille_letter[0] == letter.lower():

                if letter.isupper():

                    translation += (capital + braille_letter[1])

                else:

                    translation += braille_letter[1]

    return translation