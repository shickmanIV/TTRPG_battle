from Game import Actor

class GameController():
    # List of characters, to be sorted in initiative order
    actorList: list[Actor]

    def __init__(self) -> None:
        self.actorList = []
    
    # Add a character to the fight
    def addCharacter(self, newActor: Actor):
        self.actorList.append(newActor)

    # Start the simulation.
    def run(self) -> None:
        # Get each actor's initiative, then use the result to sort actorList
        self.rollInitiatives()
        

        roundNum = 1
        while (True):
            #Cycle through each character's turn
            

            roundNum += 1
            if (roundNum > 10):
                break

    def rollInitiatives(self) -> None:
        # For each actor, get their initiative value
        # Sort charlist by each actors initiative.
        return
    

    
