from systems.system import System
from components.action_component import ActionComponent

class BattleSystem(System):
    def __init__(self):
        self.action_queue = []

    def queue_action(self, action_type, target=None):
        self.action_queue.append(ActionComponent(action_type, target))

    def update(self, world):
        for action in self.action_queue:
            self.execute_action(action, world)
        self.action_queue.clear()

    # Placeholder
    def execute_action(self, action, world):
        if action.action_type == "attack":
            print("Player attacks!")
        elif action.action_type == "defend":
            print("Player defends!")