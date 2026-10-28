def make_hangman(secret_word):
    # 1. declare an empty list to record the guessed letters (this is the state that the closure needs to "preserve")
    guesses = []

    def hangman_closure(letter):
        # 2. add the newly guessed letter to the guesses list
        if letter not in guesses:
            guesses.append(letter)
        
        # 3. build the display string: if the letter has been guessed, display the original word, otherwise display "_"
        display_word = ""
        all_guessed = True
        
        for char in secret_word:
            if char in guesses:
                display_word += char
            else:
                display_word += "_"
                all_guessed = False # if any letter hasn't been guessed, then it's not fully guessed yet
                
        # 4. print the current progress
        print(f"Current word: {display_word}")
        
        # 5. return True (all guessed) or False (not all guessed)
        return all_guessed

    # 6. The outer function must return the inner function itself (without parentheses!)
    return hangman_closure

if __name__ == "__main__":
    # 1. ask user to set the secret word
    secret = input("Please enter the secret word for Hangman: ").strip().lower()
    
    # 2. initialize the hangman game (get the dedicated game function)
    play_hangman = make_hangman(secret)
    
    print("\nGame starts! Please guess the letters one by one.")
    
    # 3. use a while loop to continuously let the user guess until they win
    while True:
        guess_letter = input("Please guess a letter: ").strip().lower()
        
        # call the closure function to check the result
        is_won = play_hangman(guess_letter)
        
        if is_won:
            print("Congratulations! You guessed all the letters! ")
            break