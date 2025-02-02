import math
import random
from itertools import permutations

def to_ounces(x):
    return 28.3495231 * x

def to_celsius(x):
    return (5 / 9) * (x - 32)

def solve(heads, legs):
    for rabbits in range(heads + 1):
        chickens = heads - rabbits
        if (chickens * 2 + rabbits * 4) == legs:
            return chickens, rabbits
    return "this task cannot be solved"

def filter_numbers(p):
    if p < 2:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

def filter_prime(a):
    return [num for num in a if filter_numbers(num)]

def to_permutate(word):
    for i in permutations(word):
        print(''.join(i))

def word_reverse(words):
    splitted_list_words = words.split()
    return ' '.join(reversed(splitted_list_words))

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    a = [0, 0, 7]
    i = 0
    for num in nums:
        if num == a[i]:
            i += 1
        if i == len(a):
            return True
    return False

def sphere_volume_calculator(r):
    return 4 * math.pi * r ** 3 / 3

def palindrome_checker(element):
    return element == element[::-1]

def histogram(a):
    for el in a:
        print('*' * el)

def number_guess():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.\nTake a guess")
    
    guesses = 0
    my_number = random.randint(1, 20)
    
    while True:
        guessing_number = int(input())
        guesses += 1
        
        if my_number == guessing_number:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
        elif my_number > guessing_number:
            print("\nYour guess is too low.")
        else:
            print("\nYour guess is too high.")
        
        print("Take a guess.")

if __name__ == "__main__":
    grams = float(input("Grams: "))
    print("In ounces:", to_ounces(grams))

    print("In Celsius:", to_celsius(330))

    heads = int(input("Heads: "))
    legs = int(input("Legs: "))
    print(solve(heads, legs))

    a = list(map(int, input("Numbers separated by space: ").split()))
    print(filter_prime(a))

    word = input("Enter a word: ")
    to_permutate(word)

    words = input("Enter your sentence: ")
    print(word_reverse(words))

    print(has_33([1, 3, 3]))
    print(has_33([1, 3, 1, 3]))
    print(has_33([3, 1, 3]))

    print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    print(spy_game([1, 0, 2, 4, 0, 5, 7]))
    print(spy_game([1, 7, 2, 0, 4, 5, 0]))

    print(sphere_volume_calculator(5))

    word_1 = "madam"
    word_2 = "sayat"
    print(palindrome_checker(word_1))
    print(palindrome_checker(word_2))

    list_of_values = [4, 9, 7]
    histogram(list_of_values)

    number_guess()