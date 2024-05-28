from world import World
from systems.input_system import InputSystem
from systems.battle_system import BattleSystem
from event_bus import EventBus

class GameLoop:
    def __init__(self):
        self.event_bus = EventBus()
        self.world = World()
        self.input_system = InputSystem(self.event_bus)
        self.world.add_system(self.input_system, priority=1)
        self.world.add_system(BattleSystem(self.event_bus), priority=2)

    def run(self):
        loops = 0
        while True:
            # Placeholder for getting user_input
            user_input = input("Enter your command (ATTACK, DEFEND): ")
            if user_input == "QUIT" or loops > 10:
                break

            self.input_system.capture_input(user_input)
            self.world.update()
            loops += 1

    def display_all_entities(self):
        self.world.print_all_entities()

    # TODO: Implement rendering
    def render(self):
        pass #self.renderer.render(self.entity_manager)

# For debugging
if __name__ == "__main__":
    game = GameLoop()
    game.run()