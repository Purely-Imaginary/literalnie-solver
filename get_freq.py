import json

green = '***ia'
yellow = 'o'
black = 'ewrtupshjkznm'


def isValidWord(word, green, yellow, black):
    miss = False
    for idx, letter in enumerate(green):
        if letter == '*' or letter == '':
            continue
        if word[idx] != letter:
            miss = True
    if miss:
        return False
    
    for letter in yellow:
        if word.find(letter) == -1:
            miss = True;
    if miss:
        return False
    
    for letter in black:
        if word.find(letter) != -1:
            miss = True;
    if miss:
        return False
    return True



data = ""
f = open('freq2.txt')
data = json.load(f)
f.close()
solveSet = []

for wordSet in data:
    if (isValidWord(wordSet['word'], green, yellow, black)):
        solveSet.append(wordSet)

if len(solveSet) > 0:
    for solveWord in solveSet:
        print(solveWord)
else:        
    print('Getting secondary dictionary')

    data = ""
    f = open('literalnie_baza.txt')
    data = f.read().split('\n')
    f.close()
    for word in data:
        if (isValidWord(word, green, yellow, black)):
            solveSet.append(word)

    if len(solveSet) > 0:
        for solveWord in solveSet:
            print(solveWord)
    else:
        print("Nothing found :<")
