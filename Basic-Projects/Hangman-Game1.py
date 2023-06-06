import random

def hangman():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    word = random.choice(words)
    guesses = []
    attempts = 6

    while attempts > 0:
        print("\nWord:", " ".join(letter if letter in guesses else "_" for letter in word))
        print("Attempts remaining:", attempts)

        guess = input("Enter a letter: ").lower()

        if guess in guesses:
            print("You've already guessed that letter. Try again.")
            continue

        guesses.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if set(word) == set(guesses):
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("You ran out of attempts. The word was:", word)

hangman()
