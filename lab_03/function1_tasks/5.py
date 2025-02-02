from itertools import permutations

def to_permatuate(word):
    for i in permutations(word):
        print(''.join(i))

word = input("Enter a word: ")

to_permatuate(word)