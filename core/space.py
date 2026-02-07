class TopologicalSpace:
    def __init__(self, name):
        self.name = name
        self.generators = []

    def fundamental_group(self):
        return self.generators

    def __repr__(self):
        return self.name
