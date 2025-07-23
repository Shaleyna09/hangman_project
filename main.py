previous_inputs = set()
while True:
    Kartoffel = input("Enter a letter: ")
    if not (Kartoffel.isalpha() and len(Kartoffel) == 1):
        print("Please enter a single letter.")
        continue
    if Kartoffel in previous_inputs:
        print("You have already guessed that letter. Try again.")
    else:
        previous_inputs.add(Kartoffel)
        print(f"You guessed: {Kartoffel}")
