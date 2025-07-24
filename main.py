from game import HangmanGame
game = HangmanGame(word="example", guessed_letters=set(), max_errors=6, errors=0)
ze_word =  set()
while True:
    Kartoffel = input("Enter a letter: ")
    if not Kartoffel.isalpha():
        print("It must be a letter.")
        continue

    elif not len(Kartoffel) == 1:
        print("Please enter a single letter.")
        continue

    elif Kartoffel in ze_word:
        print("You have already guessed that letter. Try again.")

    elif ze_word.add(Kartoffel):
        print(f"You guessed: {ze_word}")
    else: 
        ze_word.add(Kartoffel)
        game.guess('ze_word')

    if game.is_won():
        print(f"You won! The word was: {game.word}")
        break
    elif game.is_lost():
        print(f"You lost! The word was: {game.word}")
        break
