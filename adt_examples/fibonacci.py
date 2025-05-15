"""Public module for the fib sequence class."""


class Fib:
    """Iterator yielding the Fib numbers."""

    def __init__(self):
        """Initialise class."""
        self.a = 1  # the question sucks lol
        self.b = 2  # second number

    def __iter__(self):
        return self

    def __next__(self):
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current


for n in Fib():
    print(n)
    if n >= 900:
        break
