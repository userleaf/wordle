from random import randint
from termcolor import colored
import os

os.system("rm main.bfba912f.js")
os.system("wget https://www.nytimes.com/games/wordle/main.bfba912f.js")
os.system("cat main.bfba912f.js |awk -F 'Ma=' '{if(NR==1) print $2}'| awk -F ',Oa=' '{print $1}'>words.txt")
os.system("rm main.bfba912f.js")
wordles = eval(open("words.txt", "r").read())
wordle = wordles[randint(0, len(wordles)-1)]
wordleConstant = wordle

def game():
    colorsDict = {}
    guess = input()
    if len(guess) !=5 and guess not in wordles:
        print("Yanlış karakter sayısı")
        game()

    '''
    colorsDict = {}
    greens = [index for index, letter in enumerate(guess) if letter == wordle[index]]
    yellows = [index for index, letter in enumerate(guess) if letter in wordle and Counter(guess)[letter] <= Counter(wordle)[wordle[index]] and index not in greens]
    colorsDict["greens"] = greens
    colorsDict["yellows"] = yellows
    colorsDict["grays"] = [index for index, letter in enumerate(guess) if letter not in wordle]
    for i in range(5):
        if i in colorsDict["greens"]:
            print(colored(guess[i], "green"))
        elif i in colorsDict["yellows"]:
            print(colored(guess[i], "yellow"))
        else:
            print(guess[i])
'''

def new_wordle():
    global wordle
    global wordleConstant
    wordle = wordles[randint(0, len(wordles)-1)]
    wordleConstant = wordle

def api(guess):
    global wordle
    global wordleConstant
    wordle = wordleConstant
    if len(guess) !=5:
        return False
    if guess == wordle:
        new_wordle()
        return [[0,1,2,3,4],[]]
    yellows=[]
    greens=[]
    for i in range(len(guess)):
        if guess[i] == wordle[i]:
            greens.append(i)
            wordle = wordle[:i] + "*" + wordle[i+1:]
            guess = guess[:i] + "?" + guess[i+1:]
    for index, letter in enumerate(guess):
        if letter in wordle:
            yellows.append(index)
            wordle = wordle.replace(letter, "*",1)
    return[greens, yellows]


