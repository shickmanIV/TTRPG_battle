from typing import Any
from components.component import Component
import logging

logger = logging.getLogger(__name__)

class AbilityScores(Component):
    """
    A class representing the ability scores of a character.

    Attributes:
        scores (dict): A dictionary containing the ability scores of the character.
            The keys are the ability names (str) and the values are the corresponding scores (int).
    
    Methods:
        bonus(key: str) -> int:
            Calculates the ability score bonus for a given ability.
            Returns:
                The ability score bonus (int).
        
        print_attributes(indent: str):
            Prints the ability scores and their corresponding bonuses.
    """

    def __init__(self, **args):
        """
        Initializes the AbilityScores object.

        Args:
            **args: Keyword arguments representing the ability scores.
                The keys should be the ability names (str) and the values should be the corresponding scores (int).
                If a key is not provided, the default score is 10.
        """
        self.scores = {'str': args.get('str', 10),
                       'dex': args.get('dex', 10),
                       'con': args.get('con', 10),
                       'int': args.get('int', 10),
                       'wis': args.get('wis', 10),
                       'cha': args.get('cha', 10)}
    
    def bonus(self, key: str) -> int:
        """
        Calculates the ability score bonus for a given ability.

        Args:
            key (str): The ability name.

        Returns:
            The ability score bonus (int).
        """
        try:
            value = self.scores[key]
        except KeyError:
            value = 0
            logger.error(f"KeyError: {key} is not found in {self.scores}")
        
        return int((value - 10) / 2)
    
    def print_attributes(self, indent=""):
        """
        Prints the ability scores and their corresponding bonuses.

        Args:
            indent (str): The starting indentation amount to be used for each line.
        """
        for key, value in self.scores.items():
            bonus = self.bonus(key)
            print(f"{indent}{key}: {value}\t({'+' if (bonus >= 0) else ''}{bonus})")



        
        


    

