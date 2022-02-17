# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:26:19 2021

@author: alpaylan, askafkas, mkaynarca, nbyavuz
"""


from operator import eq
from typing import Tuple

def confirmation(words:list) -> list:
    print(words)
    inp = input("\nIs the word list true? (y/n)\n")
    if inp == ("Y" or "y"):
        return words
    else:
        words = createWords()
        return words     

    
def createWords() -> list:
    empty_lines = 0
    words = []    
    while empty_lines == 0:
        inp = input("\nPlease type in your words\nSubmit empty line to stop\n")
        if inp == "":
            empty_lines=1
            confirmation(words)
        else :
            words.append(inp)         
    return words
                     

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

def simLevel(selected: list) -> int:
    inp = input(f"\nPlease input the similarity level for {selected}\nLeave empty for exact match\n")    
    if inp == "":
        likeness = len(selected)
    else : 
        likeness = int(inp)        
    return likeness

def calculateRemaining(words: list, selected: list, likeness: int) -> list:
    return [words[i] for i, elem in enumerate(selected) if likeness == elem]


def solve(words: list) -> int:
    remaining = len(words)
    tour_count = 1
    while len(words) > 1:
        similarityMatrix = createMatrix(words)
        scoreMatrix = createScore(words, similarityMatrix)
        selectedIndex, selected = calculateSelected(words,scoreMatrix)        
        print(f'\nTour {tour_count}')
        print(f'Selected = {selected}')
        likeness=simLevel(selected)
        words = calculateRemaining(words, similarityMatrix[selectedIndex], likeness)
        print(f'Remaining count = {len(words)}\n')
        tour_count = tour_count + 1
    if len(words) == 1:
        print(f'Password cracked, password = {words[0]}')
        
def main():
    words = createWords()
    solve(words)
    
    
if __name__ == "__main__":
    main()
    
