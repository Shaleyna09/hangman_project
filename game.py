from utils import get_random_word

class HangmanGame:
    def __init__(self, word=None, guessed_letters=None, max_errors=6, errors=0):
        self.__word = word or get_random_word()
        self.guessed_letters = guessed_letters or set()
        self.max_errors = max_errors
        self.errors = errors
   
    def display_word(self):
        for letter in self.word:
            if letter in self.guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, value):
        self.__word = value
    
    def process_guess(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.errors += 1
            return False
    
    def display_progress(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.__word])

    def guess(self, letter):
        if letter in self.__word:
            self.guessed_letters.add(letter)
            print("Correct guess ;)")
        else:
            self.guessed_letters.add(letter)
            self.errors += 1
            print("Wrong guess")

        print(self.display_progress())
        print(f"Errors: {self.errors}/{self.max_errors}")
    
    def is_won(self):
            return all(letter in self.guessed_letters for letter in self.word)
        
    def is_lost(self):
        return self.errors >= self.max_errors
