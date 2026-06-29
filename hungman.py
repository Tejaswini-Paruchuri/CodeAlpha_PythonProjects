import random

# List of predefined words
words = ["python", "computer", "keyboard", "developer", "internship"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_attempts = 6

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

while wrong_attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_attempts -= 1
        print("❌ Wrong Guess!")
        print("Attempts Left:", wrong_attempts)

if wrong_attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)