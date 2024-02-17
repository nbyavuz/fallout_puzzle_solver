# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:26:19 2021

@author: alpaylan, askafkas, mkaynarca, nbyavuz
"""
import colorama
import random

def testBench(numWords: int, wordLength: int):
    words = []
    for i in range(numWords):
        words.append("".join([chr(random.randint(97, 122)) for i in range(wordLength)]))
    
    password = words[random.randint(0, numWords - 1)]
    print(f"Password: {password}")
    tour = 1
    while len(words) > 1:
        print(f"Tour {tour}")
        simMatrix = createMatrix(words)
        posMatrix = createPos(simMatrix)
        scoreMatrix = createScore(posMatrix)
        index = bestIndex(scoreMatrix)
        print(f"Best word: {words[index]}\n")
        likeness = compareWords(words[index], password)
        print("\n")
        words = eliminateWords(words, index, likeness)
        tour = tour + 1
        print(f"Remaining words: {len(words)+1}\n")
    if len(words) == 1:
        print(f"The password is: {words[0]}")
        print(f"Tour count: {tour}")
    


def createWords():
    confirmed = False
    while not confirmed:
        inp = input("Write down the words you would like to use, seperated by a comma, spaces are allowed\n")
        words = inp.lower().replace(" ", "").split(",")
        if checkWordlist(words):
            inp = input("Are you sure you want to use these words? (y/n)\n")
            if inp.lower() == "y":
                confirmed = True
        else:
            print(colorama.Fore.RED + "You fucked up")
            print(colorama.Fore.RESET)
    return words


def checkWordlist(words: list):
    if len(words) != len(set(words)):
        return False
    length = len(words[0])
    for word in words:
        if len(word) != length:
            return False
    return True

def compareWords(word1: str, word2: str):
    sim = 0
    for i, c in enumerate(word1):
        if c == word2[i]:
            sim = sim + 1
    return sim
                
def createMatrix(words: list):
    if checkWordlist(words):
        simMatrix = []
        for tWord in words:
            simMatrix.append([])
            for sWord in words:
                sim = 0
                for i,c in enumerate(sWord):
                    if c == tWord[i]:
                        sim = sim + 1
                simMatrix[-1].append(sim)
        return simMatrix
    else:
        print("The word list is not valid.")
        words = createWords()
        createMatrix(words)

def createPos(simMatrix: list):
    posMatrix = []
    for simList in simMatrix:
        posMatrix.append([])
        simCounts = dict()
        for i in simList:
            simCounts[i] = simCounts.get(i, 0) + 1
        for i in range(max(simList) + 1):
            posMatrix[-1].append(simCounts.get(i, 0))
    return posMatrix

def createScore(posMatrix: list):
    scoreMatrix = []
    for posList in posMatrix:
        score = 0
        for pos in posList:
            score = score + pos*(sum(posList) - pos)
        scoreMatrix.append(score)
    return scoreMatrix


def bestIndex(scoreMatrix: list):
    return scoreMatrix.index(max(scoreMatrix))

def getLikeness():
    return int(input("Please enter the likeness level: "))
               

def eliminateWords(words: list, index: int, likeness: int):
    remaining = []
    for selected in words:
        if compareWords(selected, words[index]) == likeness:
            remaining.append(selected)
    return remaining

def solve(words: list):
    while len(words) > 1:
        simMatrix = createMatrix(words)
        posMatrix = createPos(simMatrix)
        scoreMatrix = createScore(posMatrix)
        index = bestIndex(scoreMatrix)
        print(f"Best word: {words[index]}\n")
        likeness = getLikeness()
        print("\n")
        words = eliminateWords(words, index, likeness)
    if len(words) == 1:
        print(colorama.Fore.GREEN + f"The password is: {words[0]}")
        print(colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + "You fucked up.")
        print(colorama.Fore.RESET)
        
def main():
    words = createWords()
    solve(words)

if __name__ == "__main__":
    main()
    
