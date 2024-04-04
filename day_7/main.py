import random
from hangman_words import word_list
from hangman_art import logo
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

print(f'Pssst, length of the word to guess is {word_length}.\n')

display=[]
for _ in range(word_length):
    display += "_"

print(display)
i = 0
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    if "_" not in display:
        print(f"{''.join(display)}")
        print("you win")
        end_of_game = True