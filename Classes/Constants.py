from enum import Enum

class AbilityType(Enum):
    STR = 0
    DEX = 1
    CON = 2
    INT = 3
    WIS = 4
    CHA = 5

class ProficiencyType(Enum):
    WEAPONS = 0
    ARTISANS_TOOLS = 1
    SKILLS = 2
    ARMOR = 3
    MUSICAL_INSTRUMENTS = 4
    SAVING_THROWS = 5
    OTHER = 6
    GAMING_SETS = 7
    VEHICLES = 8

class Allignment(Enum):
    UA, UNALIGNED, NONE = 0
    LG, LAWFULGOOD = 1
    LN, LAWFULNEUTRAL = 2
    LE, LAWFULEVIL = 3
    NG, NEUTRALGOOD = 4
    N, NN, NEUTRAL, TRUENEUTRAL = 5
    NE, NEUTRALEVIL = 6
    CG, CHAOTICGOOD = 7
    CN, CHAOTICNEUTRAL = 8
    CE, CHAOTICEVIL = 9


    