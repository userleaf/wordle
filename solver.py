import os
import itertools
import numpy as np
'''
os.system("rm main.bfba912f.js")
os.system("wget https://www.nytimes.com/games/wordle/main.bfba912f.js")
os.system("cat main.bfba912f.js |awk -F 'Ma=' '{if(NR==1) print $2}'| awk -F ',Oa=' '{print $1}'>words.txt")
os.system("rm main.bfba912f.js")
'''
words = eval(open("words.txt", "r").read())

# create a list of all possible combinations of yellow, green and black of length 5
colorsList = ["yellow", "green", "black"]
colorsList = list(itertools.product(colorsList, repeat=5))

def is_valid(word):
    global colors
    for index, letter in enumerate(guess):
        if colors[index] == "green":
            if not letter == word[index]:
                return False
            else:
                word = word[:index] + "*" + word[index+1:]
    
    for index, letter in enumerate(guess):
        if colors[index] == "yellow":
            if letter not in word or letter == word[index]:
                return False
            else:
                word = word.replace(letter, "*",1)

    for index, letter in enumerate(guess):
        if colors[index] == "black":
            if letter in word:
                return False
    return True


def word_score(word):
    scores = []
    global colors
    global guess
    for index,clr in enumerate(colorsList):
        colors=clr
        guess=word
        score = len(list(filter(is_valid, words)))
        if score != 0:
            scores.append(score)
    return np.std(scores)


counter=0


while len(words) > 1:
    setWords = set(words)
    guess = input("Enter your guess: ")
    colors= input("Enter your colors: ")
    colors = colors.split(" ")

    for index, color in enumerate(colors):
        if color == "y":
            colors[index] = "yellow"
        elif color == "g":
            colors[index] = "green"
        elif color == "b":
            colors[index] = "black"

    words = list(filter(is_valid, words))
    lists = []
    
    for word in words:
        lists.append([word, word_score(word)])
    lists.sort(key=lambda x: x[1])
    print(lists[0])
'''
lists = []
for word in words:
    lists.append([word, word_score(word)])
lists.sort(key=lambda x: x[1])
for i in range(50):
    print(lists[i])
'''

