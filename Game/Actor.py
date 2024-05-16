from Classes.Constants import AbilityType
from Classes.CharacterClass import DnDClass as CharClass


class Actor():
    # Currently unused
    name: str
    charClass: CharClass
    level: int
    abilityScores: dict[AbilityType, int]
    
    # Default constructor
    def __init__(self):
        self.name = ""
        self.charClass = None
        self.level = 1
        self.abilityScores = {AbilityType.STR: 10, AbilityType.DEX: 10, 
                              AbilityType.CON: 10, AbilityType.INT: 10, 
                              AbilityType.WIS: 10, AbilityType.CHA: 10}
        
    def __str__(self):
        return f"""
        name: {self.name}
        charClass: TODO: print charClass
        level: {self.level}
        abilityscores {self.abilityScores}
        """
    
    # Get the status of the actor, including:
    # - Spell slots, total and remaining
    # - Current status effects
    def getStatus(self):
        pass

    # Get the actions that the actor can perform this turn
    # To be called only once at the start of each turn
    def getActions(self) -> list:
        #TODO: Calculate available movement
        #TODO: Get current status effects
        #TODO: Optional: unavailable actions, along with reason of unavailablity
        pass

    # Perform an action, bonus action, reaction, or other
    def takeAction(self):
        pass

        



