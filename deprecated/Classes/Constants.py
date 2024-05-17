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
    UA = 0
    LG = 1
    LN = 2
    LE = 3
    NG = 4
    N = 5
    NE = 6
    CG = 7
    CN = 8
    CE = 9


    