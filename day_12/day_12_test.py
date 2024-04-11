import random
from art import logo
print(logo)

print("Welcome the Number Guessing Game! \nI'm thinking of a number between 1 and 100 \n")

original_number = random.randint(1,100)
print(original_number)
choose = input("Choose the difficulty. Type 'easy' or 'hard': ")

guess_correctly = False
def guess_number():
    guess_num = int(input("make a guess: "))
    return guess_num

def high_low(guess_num , original_number):
    global guess_correctly
    if guess_num < original_number:
        print("Too low\nTry again")
    elif guess_num > original_number:
        print("Too High\nTry again")
    elif guess_num == original_number:
        print("You guess it correctly")
        guess_correctly = True

if choose == 'easy':
    easy_decresing_num = 10
    print(f"You have {easy_decresing_num} attempts remaining to guess the number")
    for i in range(1,11):
        guess_num = int(input("make a guess: "))
        msg = high_low(guess_num , original_number)
        print(msg)
        print(f"You have {easy_decresing_num - i} attempts remaining to guess the number")
        if i == 11 and guess_correctly == False:
            print("You are out of guess ")
elif choose == 'hard':
    hard_decresing_num = 5
    print(f"You have {hard_decresing_num} attempts remaining to guess the number")
    for i in range(1,6):
        guess_num = int(input("make a guess: "))
        msg = high_low(guess_num , original_number)
        print(msg)
        print(f"You have {hard_decresing_num - i} attempts remaining to guess the number")
        if i == 5 and guess_correctly == False:
            print("You are out of guess ")




