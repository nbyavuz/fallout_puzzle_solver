"""
Created on Wed Sep  8 15:42:43 2021

@author: alpaylan, askafkas, mkaynarca, nbyavuz
"""


import json
import string
import random
from operator import eq
from typing import Tuple

CONF_FILE_NAME = 'options.json'

def readJson(fileName: str) -> object:
    with open(fileName) as f:
        return json.load(f)

def createWords(settings: object) -> list:
    returnList = []
    alphabet = random.sample(list(string.ascii_uppercase), settings['alphabet_count'])
    for i in range(settings['word_count']):
        elem = [random.choice(alphabet) for _ in range(settings['word_length'])]
        returnList.append(elem)
    return returnList

def createMatrix(words: list) -> list:
    similarityMatrix = []
    for word in words:
        similarityMatrix.append([])
        for similar_word in words:
            similarityMatrix[-1].append(sum(map(eq, word, similar_word)))
    return similarityMatrix 

def createScore(words: list , similarityMatrix: list) -> list:
    possibilityMatrix = []
    for i in range(len(similarityMatrix)):
        possibilityMatrix.append([])
        for j in (range(0,len(words[0]) + 1)):
            possibilityMatrix[-1].append(((similarityMatrix[i].count(j)) * (len(similarityMatrix) - similarityMatrix[i].count(j)))/len(similarityMatrix))
    scoreMatrix = []
    for i in range(len(possibilityMatrix)):
        scoreMatrix.append([])
        scoreMatrix[-1] = sum(possibilityMatrix[i])
    return scoreMatrix           

def calculateSelected(words:list , scoreMatrix: list) -> Tuple[int, list]:
    selectedIndex = scoreMatrix.index(max(scoreMatrix))
    return selectedIndex, words[selectedIndex]

def calculateRemaining(words: list, selected: list, likeness: int) -> list:
    return [words[i] for i, elem in enumerate(selected) if likeness == elem]

def solve(words: list) -> int:
    remaining = len(words)
    password = random.choice(words)
    print(f'Password = {password}')
    tour_count = 1
    while len(words) > 1:
        similarityMatrix = createMatrix(words)
        scoreMatrix = createScore(words, similarityMatrix)
        selectedIndex, selected = calculateSelected(words,scoreMatrix)
        likeness = sum(map(eq, selected, password))
        words = calculateRemaining(words, similarityMatrix[selectedIndex], likeness)
        print(f'\nTour {tour_count}')
        print(f'Selected = {selected} and likeness = {likeness}')
        print(f'Remaining count = {len(words)}\n')
        tour_count = tour_count + 1
    if len(words) == 1 and words[0] == password:
        print(f'Password cracked, password = {words[0]}')
    else:
        print(f'Something is wrong, words = {words}\npassword = {password}')


    
    
def main():
    settings = readJson(CONF_FILE_NAME)
    print(f'\nWord count = {settings["word_count"]}')
    print(f'Word length = {settings["word_length"]}')
    print(f'Alphabet count = {settings["alphabet_count"]}\n')
    words = createWords(settings)
    solve(words)


if __name__ == "__main__":
    main()
    
    
