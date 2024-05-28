from systems.system import System
from components.action_component import ActionComponent

class BattleSystem(System):
    def __init__(self, event_bus):
        self.action_queue = []
        event_bus.subscribe("ATTACK", self)
        event_bus.subscribe("DEFEND", self)

    def handle_event(self, event):
        if event.type == "ATTACK":
            self.queue_action("attack")
        elif event.type == "DEFEND":
            self.queue_action("defend")

    def queue_action(self, action_type, target=None):
        self.action_queue.append(ActionComponent(action_type, target))

    def update(self, world):
        # Process the action queue and perform actions
        pass