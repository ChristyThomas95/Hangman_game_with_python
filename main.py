import random
from Words import word_list

# ------------------------Updating the word lists from the words.py--------------------------------------
selected_word = random.choice(word_list)
word_length = len(selected_word)

game_over = False
chances = 6
#----------------------------------- Game Functions____________________________________________________________
from Game_art import logo
print(logo)

display = []
for _ in range(word_length):
    display +="_"

while not game_over:
    guess = input("Guess a letter to save a humana").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = selected_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in selected_word:
        print(f"You guessed {guess}, wrong letter. You lose a life.")
        chances -= 1
        if chances == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    from Game_art import stages

    print(stages[chances])

