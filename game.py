class HangmanGame:
    def __init__(self, word, guessed_letters, max_errors, errors):
        self.word = word
        self.guessed_letters = guessed_letters
        self.max_errors = max_errors
        self.errors = errors
   
    def display_word(self):
        for letter in self.word:
            if letter in self.guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
    
    def process_guess(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.errors += 1
            return False
    
    def is_won(self):
        return all(letter in self.guessed_letters for letter in self._word)
    
    def is_lost(self):
        tries_left = self.max_errors - self.errors
        print(f"You have {tries_left} tries left.")
    
    def display_progress(self):
        display = ""
        for char in self.word:
            if not char.isalpha():
                display += char + " "
            elif char in self.guessed_letters:
                display += char + " "
            else:
                display += "_ "
        print(display.strip())