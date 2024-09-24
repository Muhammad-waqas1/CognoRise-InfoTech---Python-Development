import random

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript', 'swift', 'django', 'flask']
    word = random.choice(words)
    guessed_word = ['_' for _ in word]
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"\n{' '.join(guessed_word)}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            for idx, char in enumerate(word):
                if char == guess:
                    guessed_word[idx] = char
            print(f"Good guess: {guess}")
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")
        
        if '_' not in guessed_word:
            print(f"Congratulations! You guessed the word: {''.join(guessed_word)}")
            break
    else:
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
