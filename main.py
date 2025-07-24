from game import HangmanGame
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
    
    else:
        previous_inputs.add(Kartoffel)
        print(f"You entered: {Kartoffel}")
        print(f"You guessed: {previous_inputs}")