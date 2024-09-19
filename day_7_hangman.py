import random
from utils.hangman import word_list, HANGMAN_PICS

player_life = 7
word = random.choice(word_list)
word_len = len(word)

letter_guess = ''
for length in range(word_len):
    letter_guess += '_'
print(letter_guess)

fail_count = 0
pass_count = 0
letter_guess_list = list(letter_guess)
while letter_guess != word and player_life != 0:
    user_input = input("Guess your letter: ").lower()
    if user_input in word:
        pass_count += 1
        for index, letter in enumerate(word):
            if word[index] == user_input and user_input != letter_guess[index]:
                letter_guess_list[index] = user_input
                break
    else:
        player_life -= 1
        fail_count += 1
        print(HANGMAN_PICS[fail_count - 1])
    letter_guess = ''.join(letter_guess_list)
    print(letter_guess)
    word_len -= 1
    if word == letter_guess:
        break

if fail_count == 6 or word != letter_guess:
    print("GAME OVER. YOUR MAN DIED!")
else:
    print("YOU WON. YOU SAVED YOUR MAN")
