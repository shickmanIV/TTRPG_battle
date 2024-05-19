from entities.entity_manager import EntityManager
from systems.health_system import HealthSystem
from ui.renderer import Renderer
from ui.user_input import UserInput
import logging # Run with "--log=INFO"

class GameLoop:
    def __init__(self):
        self.entity_manager = EntityManager()
        self.systems = []
        self.systems.append(HealthSystem())
        self.renderer = Renderer()
        self.user_input = UserInput()

    def run(self):
        loops = 0
        while True:
            self.process_input()
            self.update()
            self.render()
            loops += 1
            if loops > 50:
                break

    def display_all_entities(self):
        self.entity_manager.print_all_entities()

    # Get user inputs, then execute the corresponding commands.
    def process_input(self):
        self.user_input.get_input()
        
    def update(self):
        for system in self.systems:
            system.update(self.entity_manager)

    def render(self):
        pass #self.renderer.render(self.entity_manager)

# For debugging
if __name__ == "__main__":
    game = GameLoop()
    game.run()