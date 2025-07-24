from game import HangmanGame

game = HangmanGame()
ze_game = set()

while True:
    kartoffel = input('Enter a letter: ')
    if not len(kartoffel) == 1:
        print('It must be a single character.')
        continue
    elif not kartoffel.isalpha():
        print('It must be a letter')
        continue
    elif kartoffel in ze_game:
        print("You've already tried this letter. Try again.")
    else: 
        ze_game.add(kartoffel)
        game.guess(kartoffel)

    if game.is_won():
        print(f"You won! The word was: {game.word}")
        break
    elif game.is_lost():
        print(f"You lost! The word was: {game.word}")
        break
