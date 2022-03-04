import os
import itertools
import numpy as np
import wordle as w
from collections import Counter
'''
os.system("rm main.bfba912f.js")
os.system("wget https://www.nytimes.com/games/wordle/main.bfba912f.js")
os.system("cat main.bfba912f.js |awk -F 'Ma=' '{if(NR==1) print $2}'| awk -F ',Oa=' '{print $1}'>words.txt")
os.system("rm main.bfba912f.js")
'''
words = eval(open("words.txt", "r").read())
wordsConstant = words
# create a list of all possible combinations of yellow, green and black of length 5
colorsList = ["yellow", "green", "black"]
colorsList = list(itertools.product(colorsList, repeat=5))

def is_valid(word):
    occurenceWord = []
    global colors
    global guess
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


iterations = 500
counters = []
for ij in range(iterations):
    words = wordsConstant
    guess = "slate"
    greens,yellows = w.api(guess)
    counter = 1
    while len(greens) < 5:
        counter += 1
        colors=[]
        for i in range(5):
            if i in greens:
                colors.append("green")
            elif i in yellows:
                colors.append("yellow")
            else:
                colors.append("black")
        words = list(filter(is_valid, words))
        word_scores = [[word,word_score(word)] for word in words]
        word_scores = sorted(word_scores, key=lambda x: x[1])
        try:
            guess = word_scores[0][0]
        except:
            print(guess,colors)
        greens,yellows=w.api(guess)
    counters.append(counter)
    print("on guess {}".format(ij))


print(np.mean(counters), np.std(counters), np.min(counters), np.max(counters), Counter(counters))
