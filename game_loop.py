from world import World
from systems.input_system import InputSystem
from systems.battle_system import BattleSystem
from systems.health_system import HealthSystem
from event_bus import EventBus

class GameLoop:
    def __init__(self):
        """
        Initializes a GameLoop object.

        This class represents the main game loop that controls the flow of the game.
        It initializes the event bus, world, and various systems used in the game.

        Attributes:
        - event_bus (EventBus): The event bus used for communication between systems.
        - world (World): The game world that holds all the entities and systems.
        - input_system (InputSystem): The input system responsible for capturing user input.
        """
        self.event_bus = EventBus()
        self.world = World()
        self.input_system = InputSystem(self.event_bus)
        self.world.add_system(self.input_system, priority=0)
        self.world.add_system(HealthSystem(self.event_bus), priority=2)
        self.world.add_system(BattleSystem(self.event_bus), priority=2)

    def run(self):
        """
        Runs the game loop.

        This method starts the game loop and continues until the user enters "QUIT" or the loop count exceeds 10.
        It captures user input, updates the world, and increments the loop count.

        Returns:
        - None
        """
        loops = 0
        while True:
            user_input = input("Enter your command (ATTACK, DEFEND): ")
            if user_input == "QUIT" or loops > 10:
                break

            self.input_system.capture_input(user_input)
            self.world.update()
            loops += 1

    def display_all_entities(self):
        """
        Displays all entities in the game world.

        This method prints all the entities currently present in the game world.

        Returns:
        - None
        """
        self.world.print_all_entities()

    def render(self):
        """
        Renders the game world.

        This method is responsible for rendering the game world.
        It is currently a placeholder and does not have any implementation.

        Returns:
        - None
        """
        pass

# For debugging
if __name__ == "__main__":
    game = GameLoop()
    game.run()