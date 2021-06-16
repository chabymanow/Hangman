# Hangman game from Chabymanow                                                                                                            #
# You can play against another player or the CPU.                                                                                         #
# The CPU has a database with 212 words. You can edit this in the words.tx file.                                                          #

import random
from os import system, name
import os
import subprocess
import sys

basicLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
usedLetters = []
goodLetters = []
guessWord = ""
guesses = 0
myMessage = ""
running = True

def printScaffold(guesses): # prints the scaffold
		if (guesses == 0):
				print ("_________")
				print ("|	 |")
				print ("|")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 1):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 2):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	 |")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (guesses == 3):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (guesses == 4):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (guesses == 5):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ ")
				print ("|________")
		elif (guesses == 6):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ \ ")
				print ("|________")
				print ("\n")
                
def myClear():
    if name == 'nt':
        _ = system ('cls')
        
    else:
        _= system('clear')
        
def getWord():  
    #my_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
    lines = open("words.txt").read().splitlines()
    ranNum = len(lines)
    x = random.randint(0, ranNum)
    word = lines[x-1]
    return word
    
def printLetters():
    for x in range(len(basicLetters)):
        l = basicLetters[x]
        if l in usedLetters:
            print(" | "+" ", end="")
        else:
            print(" | "+l.upper(), end="")

def printWord(letter):
    global guessWord, running
    
    match = 0
    for x in range(len(guessWord)):
        if guessWord[x] in goodLetters:
            print(guessWord[x].upper()+" ", end="")
            match += 1
        else:
            print("_ ", end="")
    if match == len(guessWord):
        running = False
        drawScreen(1)
   
def printMessage(message):
    return message   
 
def game():
    global running, guessWord, myMessage, guesses
    
    while running:
        myClear()    
        print("\n")
        printWord("")
        print("\n")
        printScaffold(guesses)
        print("\n") 
        print(printMessage(myMessage))
        print("\n")
        printLetters()
        guessLetter = str(input("\n\nGuess a letter: "))
        if len(guessLetter) > 1:
            myMessage = "Only one letter please!"
        elif guessLetter.isalpha() == False:
            myMessage = "Please use only letter from the list above!"
        elif guessLetter == "":
            myMessage = "Enter at least one letter please!"
        elif guessLetter in usedLetters:
            myMessage = "You already guessed that letter. Choose an another one please!"
        else:        
            usedLetters.append(guessLetter)
            if guessLetter in guessWord:
                goodLetters.append(guessLetter)
                myMessage = "Good guess!"
            else:
                myMessage = "Nope, it`s not good."
                guesses += 1        
        if guesses == 6:
            running = False
            drawScreen(2)

def drawScreen(succes):
    if succes == 1:
        myClear()
        print("\nYOU WIN!\n The secret word was: {}".format(guessWord.upper()))
        print("\n")
        print("Would you like to play again?")
        print("Type 1 for yes or 2 for no.")
        choose = int(input(""))
        if choose == 1:
            menu()
        elif choose == 2:
            sys.exit()
    elif succes == 2:
        myClear()
        printScaffold(6)
        print("\n")
        print("\nSorry, you LOSE\n The secret word was: {}".format(guessWord.upper()))
        print("\n")
        print("Would you like to play again?")
        print("Type 1 for yes or 2 for no.")
        choose = int(input(""))
        if choose == 1:
            menu()
        elif choose == 2:
            sys.exit()
        
def singleGame():
    global running, guessWord
    
    myClear()
    guessWord = str(input("Please give a secret word: "))
    running = True
    game()
    
def multiGame():
    global running, guessWord
        
    guessWord = getWord()
    running = True
    game()
        
def menu():
    global running, guessWord, myMessage, guesses
    
    myClear()
    usedLetters.clear()
    goodLetters.clear()
    guesses = 0
    myMessage = ""
    print("\n\n\n")
    print("     ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗")
    print("     ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║")
    print("     ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║")
    print("     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║")
    print("     ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║")
    print("     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝")
    print("\n")
    print("     Menu:\n      1: Player VS Player\n      2: Player VS CPU\n      3: Exit\n")     
    menuSelect = int(input(""))       
    if menuSelect == 1:
        singleGame()
    elif menuSelect == 2:
        multiGame()
    else:
        sys.exit()

running = False
menu()