def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join([char if char in guesses else "_" for char in secret_word])
        print(display)
        return all(char in guesses for char in secret_word)

    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter the secret word: ")
    hangman = make_hangman(secret)

    while True:
        guess = input("Enter a letter: ")
        if hangman(guess):
            print("You guessed the word!")
            break
