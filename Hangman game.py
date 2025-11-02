# -*- coding: utf-8 -*-
"""
Created on Thu May 15 17:23:51 2025

@author: Manisha
"""

import random

words = ["COMPUTER", "MANGO", "PRINTER", "HAND"]
Word = random.choice(words)
Totalchances = 7
gussedword = "_"*(len(Word))

print("WelCome to HANGMAN")

while Totalchances != 0:
    print(gussedword)
    letter = input("Guess a letter: ").upper()
    if letter in Word:
        for i in range(len(Word)):
            if Word[i] == letter:
                gussedword = gussedword[:i] + letter + gussedword[i+1:]
                
        if gussedword == Word:
            print("Congratulations...... you won the game:)")
            break
            
    else:
        Totalchances -=1
        print("Incorrect guess")
        print("Total remaining chances are: ", Totalchances)
        
else:
    print("All the chances exausted")
    print("you lose")
    
print("The correct word is: ", Word)
