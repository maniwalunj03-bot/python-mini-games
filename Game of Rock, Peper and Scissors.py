# -*- coding: utf-8 -*-
"""
Created on Thu May 15 17:51:49 2025

@author: Manisha
"""
import random


print("Welcome to the game of Rock, Peper and Scissors.")

userscore = 0
computerscore = 0
tie = 0

name = input("Enter your name here: ")

print("""
      The winning rules of the game are : 
          between rock and paper: Paper wins
          between rock and scissors: rock wins
          between paper and scissors: scissors wins""")
          
while True:
    print("Choose between the following: \nPress 1 for rock. \nPress 2 for\
          Paper. \nPress 3 for scissors")
    user_choice = int(input("Enter your choice in between 1 to 3: "))
    
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter a valid option: "))
        
    if user_choice == 1:
        UC = "Rock"
        
    elif user_choice == 2:
        UC = "Paper"
        
    else:
        UC = "Scissors"
        
    print(name, "'s choice is", UC)
    print()
    print("Now it is computers turn")
    
    Comp_choice = random.randint(1,3)
    if Comp_choice == 1:
        CC = "Rock"
        
    elif Comp_choice == 2:
        CC = "Paper"
        
    else:
        CC = "Scissors"
        
    print("Computers choice is", CC)
    
    if (UC == "Paper" and CC == "Rock") or (UC == "Rock" and CC == "Paper"):
        result = "Paper"
        print("****** Paper wins ******")
    elif (UC == "Scissors" and CC == "Rock") or (UC == "Rock" and CC == "Scissors"):
        result = "Rock"
        print("****** Rock wins ******")
    elif (UC == CC):
        result = "tie"
        print("It's tie")
    else:
        result = "Scissors"
        print("******* Scissors wins ******")

    if result == "tie":
        tie += 1
    elif result == UC:
        print(name, "wins")
        userscore += 1
    else:
        print("Computer wins")
        computerscore += 1
    
    print("User's score is", userscore)
    print("Computer's score is", computerscore) 
    print("Ties are", tie)

    repeat = input("Do you want to play again? (Yes/No): ")
    if repeat == "No" or repeat == "no":
        break
print("Thank you for playing the game.")
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    