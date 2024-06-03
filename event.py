class Event:
    """
    Represents an event in a TTRPG battle.

    Attributes:
        type (str): The type of the event.
        data (Any): Additional data associated with the event.
    """

    def __init__(self, type, data=None):
        self.type = type
        self.data = data
