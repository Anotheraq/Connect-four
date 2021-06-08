class ImpossibleMoveException(Exception):
    def __init__(self, column, message="Can't drop here!"):
        self.column = column
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.column + 1} -> {self.message}'
