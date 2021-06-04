import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list


chosen_word = random.choice(word_list)
guessed_letters = []
print(logo)
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

lives = 7
while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess not in guessed_letters:
        guessed_letters.append(guess)

        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess

        print (display)
        if guess not in chosen_word:
            print("\nletter " + guess + " is not in the word")
            lives -= 1
        if lives < 7:
            print(stages[lives])
            if lives == 0:
                print("You lose.")
                print("Answer: " + chosen_word)
                quit()
    else:
        print("You already guessed this letter: " + guess)

print("You win.")