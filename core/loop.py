from group import Word

class Loop:
    def __init__(self, word, basepoint="*"):
        self.word = word
        self.basepoint = basepoint

    def homotopic_to(self, other):
        return self.word.letters == other.word.letters

    def __repr__(self):
        return f"Loop({self.word})"
