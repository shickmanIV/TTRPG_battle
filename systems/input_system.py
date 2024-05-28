from systems.system import System
from systems.battle_system import BattleSystem

# Not technically a system, 
class InputSystem():
    def __init__(self):
        self.commands = []

    def capture_input(self, user_input):
        self.commands.append(user_input)

    def process_input(self, world):
        for command in self.commands:
            self.execute_command(command, world)
        self.commands.clear()

    def execute_command(self, command, world):
        if command == "ATTACK":
            world.get_system(BattleSystem).queue_action("attack")
        elif command == "DEFEND":
            world.get_system(BattleSystem).queue_action("defend")