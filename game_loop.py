from entities.entity_manager import EntityManager
from systems.health_system import HealthSystem
from ui.renderer import Renderer
from ui.user_input import UserInput

class GameLoop:
    def __init__(self):
        self.entity_manager = EntityManager()
        self.health_system = HealthSystem()
        self.renderer = Renderer()
        self.user_input = UserInput()

    def run(self):
        while True:
            self.process_input()
            self.update()
            self.render()

    def process_input(self):
        self.user_input.get_input()

    def update(self):
        self.health_system.update(self.entity_manager)

    def render(self):
        self.renderer.render(self.entity_manager)

if __name__ == "__main__":
    game = GameLoop()
    game.run()