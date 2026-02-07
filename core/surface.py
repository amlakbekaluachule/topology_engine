from group import Generator, Word
from space import TopologicalSpace

class Surface(TopologicalSpace):
    def __init__(self, genus, name=None):
        super().__init__(name or f"Surface(g={genus})")
        self.genus = genus
        self.generators = []

        for i in range(genus):
            a = Generator(f"a{i+1}")
            b = Generator(f"b{i+1}")
            self.generators.append((a, b))

    def fundamental_relation(self):
        word = Word([])
        for a, b in self.generators:
            word *= Word([a, b, a.inverse(), b.inverse()])
        return word

    def describe_pi1(self):
        gens = []
        for a, b in self.generators:
            gens.append(a.name)
            gens.append(b.name)
        return f"π₁ = ⟨{', '.join(gens)} | ∏[aᵢ,bᵢ]=e⟩"
