class Alphabet:
    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration

alfabet = Alphabet()

for letter in alfabet:
    print(letter)
