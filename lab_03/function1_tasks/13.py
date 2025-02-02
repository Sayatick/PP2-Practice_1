import random

def number_guess():
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.\nTake a guess")
    
    guesses = 0
    my_number = random.randint(1, 20)
    
    while True:
        guessing_number = int(input())
        guesses += 1
        
        if my_number == guessing_number:
            print(f"Good job, KBTU! You guessed my number in {guesses} guesses!")
            break
        elif my_number > guessing_number: print("\nYour guess is too low.")
        else: print("\nYour guess is too high.")
        
        print("Take a guess.")

number_guess()