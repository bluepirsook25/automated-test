class Accumulator:
    """A simple accumulator class that keeps track of a count."""

    def __init__(self) -> None:
        self._count = 0

    @property
    def count(self) -> int:
        return self._count

    def add(self, more=1) -> None:
        self._count += more
