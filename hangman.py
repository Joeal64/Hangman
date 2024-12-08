import random

def hangman():
    words = ["apple", "luther", "jazz", "spire", "galaxy", "radio", "orange", "whisper", "cactus", "ocean"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    while attempts > 0:
        print(f"\nWord: {' '.join(guessed)}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = letter
        else:
            print("Wrong guess!")
            attempts -= 1

        guessed_letters.add(guess)

        if "_" not in guessed:
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

hangman()