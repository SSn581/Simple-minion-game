# play the game
while max_guesses - len(incorrect_letters) > 0:
    # display the game state
    display_game_state()
    
    # ask the user to guess a letter
    guess = input('Guess a letter: ').lower()
    
    # make sure the input is a single letter
    if len(guess) != 1:
        print('Please guess a single letter')
        continue
    
    # if the letter has already been guessed, tell the user and continue
    if guess in correct_letters or guess in incorrect_letters:
        print('You already guessed that letter')
        continue
    
    # if the guess is correct, add it to the set of correct letters
    if guess in word:
        correct_letters.add(guess)
        if len(correct_letters) == len(set(word)):
            print('You win! The word was', word)
            break
    # if the guess is incorrect, add it to the set of incorrect letters
    else:
        incorrect_letters.add(guess)
    
# if the user runs out of guesses, they lose
else:
    print('You lose! The word was', word)
