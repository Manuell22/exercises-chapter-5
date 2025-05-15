"""The deque module."""


class Deque:
    """Class defining a deque."""

    def __init__(self, n):
        """Create the ring buffer deque."""
        self.deque = [None] * n
        self.size = n
        self.front = 0
        self.back = 0

    def append(self, x):
        """Append to the deque."""
        self.deque[self.back] = x
        if self.back == self.front:
            if self.front == 0:
                self.front = self.size - 1
            else:
                self.front -= 1
        if self.back == self.size - 1:
            self.back = 0
        else:
            self.back += 1

    def appendleft(self, x):
        """Append to the left of it."""
        self.deque[self.front] = x
        if self.back == self.front:
            if self.back == self.size - 1:
                self.back = 0
            else:
                self.back += 1
        if self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1

    def pop(self):
        """Pop from the back."""
        temp = self.deque[self.back]
        self.deque[self.back] = None
        if self.back == self.size - 1:
            self.back = 0
        else:
            self.back += 1
        return temp

    def popleft(self):
        """Pop fron the front."""
        temp = self.deque[self.front]
        self.deque[self.front] = None
        if self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1      
        return temp

    def peek(self):
        """Peek from the back."""
        if self.back == 0:
            return self.deque[self.size - 1]
        else:
            return self.deque[self.back - 1]

    def peekleft(self):
        """Peek from the front."""
        if self.front == self.size - 1:
            return self.deque[0]
        else:
            return self.deque[self.front]

    def __len__(self):
        """Return length."""
        count = 0
        for i in self.deque:
            if i is not None:
                count += 1
        return count

def __iter__(self):
    return self

def __next__(self):
    length = len(self)
    self.a = self.deque[self.front]
