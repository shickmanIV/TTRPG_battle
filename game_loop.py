from entities.entity import Entity
from systems.health_system import HealthSystem
from ui.renderer import Renderer
from ui.user_input import UserInput
import logging # Run with "--log=INFO"

from world import World
from systems.input_system import InputSystem
from systems.battle_system import BattleSystem

class GameLoop:
    def __init__(self):
        self.world = World()
        self.input_system = self.world.add_system(InputSystem())
        self.world.add_system(BattleSystem())
        self.world.add_system(HealthSystem())
        self.renderer = Renderer()

    def run(self):
        loops = 0
        while True:
            # Placeholder for getting user_input
            user_input = input("Enter your command (ATTACK, DEFEND): ")
            if user_input == "QUIT" or loops > 10:
                break
            self.input_system.capture_input(user_input)
            self.input_system.process_input(self.world)
            self.world.update()
            loops += 1

    def display_all_entities(self):
        self.world.print_all_entities()

#    def render(self):
#        pass #self.renderer.render(self.entity_manager)

# For debugging
if __name__ == "__main__":
    game = GameLoop()
    game.run()
