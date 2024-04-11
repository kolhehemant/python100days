import random
from art import logo, vs
from game_data import  data
from clear_screen import clear
# ========= sudo code logic =========
# Display art
# Generate random account from the game data
# Format the account data
# Ask user for the guess

#Check if user guess is correct
## Get the followers count for each account
## check user guess is correct corresponding to count for each account

# Give user feedback on their guess
# score keeping
# MAke the repeatable , if user guess is correct and in this case account b should become account A
# and gues another new account should get assigned to account B

# If user guess is incorrect display the score and terminate the game

# =========== start the code
# Generate random account from the game data

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")

def get_random_account():
    """Get data from random accoun"""
    return random.choice(data)

## check user guess is correct corresponding to count for each account
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
#MAke the repeatable
account_b = random.choice(data)

while game_should_continue:

    # Format the account data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    # Format the account data

    # Format the account data
    formattted_act_a = format_data(account_a)
    formattted_act_b = format_data(account_b)

    print(f"Compare A: {formattted_act_a}.")
    print(vs)
    print(f"Against B: {formattted_act_b}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    #print(f"a followers count {a_follower_count} and {b_follower_count}")
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    clear
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")