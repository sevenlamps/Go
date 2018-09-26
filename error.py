class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InvalidNumberOfStones(Error):
    def __init__(self):
        pass


class BoardNotEmpty(Error):
    def __init__(self):
        pass


class BadVertexList(Error):
    def __init__(self):
        pass


class IllegalMove(Error):
    def __init__(self, message):
        self._message = message


class CannotUndo(Error):
    def __init__(self, message):
        self._message = message


class InvalidOppositeColor(Error):
    def __init__(self):
        pass
