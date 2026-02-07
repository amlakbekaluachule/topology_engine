class CoveringSpace:
    def __init__(self, base_space, degree):
        self.base_space = base_space
        self.degree = degree

    def lift_loop(self, loop):
        if loop.word.is_trivial():
            return "Closed lift"
        return "Lift may not close"

    def __repr__(self):
        return f"{self.degree}-sheeted cover of {self.base_space}"
