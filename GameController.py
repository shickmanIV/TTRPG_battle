
class Character():
    pass
#
class GameController():
    
    charList: set[Character]
    initiatives: dict[Character: int]

    def __init__(self) -> None:
        self.charList = []
    
    # Add a character to the fight.
    def addCharacter(self, newChar: Character):
        self.charList.append(Character)

    # Start the simulation.
    def run(self) -> None:
        roundNum = 1
        initiatives = self.rollInitiatives()
        #TODO: Roll initiative

        while (True):
            #Cycle through each character's turn
            

            roundNum += 1
            if (roundNum > 10):
                break

    def rollInitiatives(self) -> dict[Character: int]:
        # For each character 'actor', get their initiative value
        # and save it to initiatives['actor']

        #Returns a sorted list of 
        return 
    
