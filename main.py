from game import HangmanGame
game = HangmanGame(word="example", guessed_letters=set(), max_errors=6, errors=0)
previous_inputs = set()
while True:
    Kartoffel = input("Enter a letter: ")
    if not Kartoffel.isalpha():
        print("It must be a letter.")
        continue

    elif not len(Kartoffel) == 1:
        print("Please enter a single letter.")
        continue

    elif Kartoffel in previous_inputs:
        print("You have already guessed that letter. Try again.")

    elif previous_inputs.add(Kartoffel):
        print(f"You guessed: {previous_inputs}")
    
    elif previous_inputs.add(Kartoffel):
        print(f"You entered: {Kartoffel}")
        print(f"You guessed: {previous_inputs}")
    
    elif game.is_won():
       print(f"You won! The word was: {game.word}")
       break
    elif game.is_lost():
        print(f"You lost! The word was: {game.word}")
        break