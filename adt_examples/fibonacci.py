class Fib:
    """Iterator yielding the Fib numbers."""

    def __init__(self):
        """Initialise class."""
        self.a = 0  # First fib number
        self.b = 1  # second number

    def __iter__(self):
        return self

    def __next__(self):
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current
