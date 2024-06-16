from components.component import Component

class HealthComponent(Component):
    """
    A class representing the health component of a character.

    Attributes:
        current_hp (int): The current hit points of the character.
        max_hp (int): The maximum hit points of the character.
        temp_hp (int): Temporary hit points that can be added to the character's current hit points.
    """

    def __init__(self, max_hp):
        self.current_hp = max_hp
        self.max_hp = max_hp
        self.temp_hp = 0

    def print_attributes(self, indent=""):
        """
        Prints the attributes of the HealthComponent.

        Args:
            indent (str, optional): The starting indentation amount to be used for printing. Defaults to "".
        """
        print(indent + "current_hp:", self.current_hp)
        print(indent + "max_hp:", self.max_hp)
        print(indent + "temp_hp:", self.temp_hp)
