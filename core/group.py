class Generator:
    def __init__(self, name):
        self.name = name

    def inverse(self):
        return Generator(self.name + "^{-1}")

    def __repr__(self):
        return self.name


class Word:
    def __init__(self, letters):
        self.letters = letters
        self.reduce()

    def reduce(self):
        reduced = []
        for g in self.letters:
            if reduced and reduced[-1].name == g.inverse().name:
                reduced.pop()
            else:
                reduced.append(g)
        self.letters = reduced

    def __mul__(self, other):
        return Word(self.letters + other.letters)

    def inverse(self):
        inv = [g.inverse() for g in reversed(self.letters)]
        return Word(inv)

    def is_trivial(self):
        return len(self.letters) == 0

    def __repr__(self):
        if not self.letters:
            return "e"
        return "".join(str(g) for g in self.letters)
