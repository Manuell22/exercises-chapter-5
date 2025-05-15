"""Reverse polish calculator module."""
from numbers import Number
import math as m


class RPCalc:
    """Class to implement the RPC."""

    def __init__(self):
        """Instantiate object."""
        self.stack = []

    def pop(self):
        """Pop method."""
        if len(self.stack):
            return self.stack.pop()

    def push(self, n):
        """Push method."""
        if isinstance(n, Number):
            self.stack.append(n)
        supported = ["+", "-", "*", "/", "sin", "cos"]
        if n in supported:
            if n == "sin":
                self.stack.append(m.sin(self.stack.pop()))
            elif n == "cos":
                self.stack.append(m.cos(self.stack.pop()))
            else:
                n2 = self.stack.pop()
                n1 = self.stack.pop()
                if n == "+":
                    self.stack.append(n1 + n2)
                elif n == "-":
                    self.stack.append(n1 - n2)
                elif n == "/":
                    self.stack.append(n1 / n2)
                elif n == "*":
                    self.stack.append(n1 * n2)

    def peek(self):
        """Peek method."""
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)
