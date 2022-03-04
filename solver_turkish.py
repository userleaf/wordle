import os
import itertools
import numpy as np
words = open("turkce_kelimeler.txt", "r")
words = words.readlines()
words=[x[:-1].lower() for x in words if len(x) == 6 and " " not in x]
# create a list of all possible combinations of yellow, green and black of length 5
colorsList = ["yellow", "green", "black"]
colorsList = list(itertools.product(colorsList, repeat=5))

def is_valid(word):
    occurenceWord = []
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
                indices = [i for i, x in enumerate(guess) if x == letter and colors[i] == "yellow"]
                occurenceWord = [i for i, x in enumerate(word) if x == letter]
                if len(indices) > len(occurenceWord):
                    return False
            
    for index, letter in enumerate(guess):
        if colors[index] == "black" and index not in occurenceWord:
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
