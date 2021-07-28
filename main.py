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

def calculateSelected(words: list) -> Tuple[int, list]:
    selectedIndex = random.choice(range(len(words)))
    return selectedIndex, words[selectedIndex]

def calculateRemaining(words: list, selected: list, likeness: int) -> list:
    returnList = []
    for i, elem in enumerate(selected):
        if likeness == elem:
            returnList.append(words[i])
    return returnList

def solve(words: list) -> int:
    remaining = len(words)
    password = random.choice(words)
    print(f'Password = {password}')
    tour_count = 1
    while len(words) > 1:
        similarityMatrix = createMatrix(words)
        selectedIndex, selected = calculateSelected(words)
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
