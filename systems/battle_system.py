from systems.system import System
from components.action_component import ActionComponent
from world import World

class BattleSystem(System):
    """
    A class representing the battle system in a TTRPG game.

    Attributes:
        action_queue (list): A list to store the queued actions.
    
    Methods:
        __init__(self, event_bus): Initializes the BattleSystem object.
        handle_event(self, event): Handles the events received from the event bus.
        queue_action(self, action_type, target=None): Adds an action to the action queue.
        update(self, world): Updates the battle system based on the current state of the world.
    """

    def __init__(self, event_bus):
        """
        Initializes the BattleSystem object.

        Args:
            event_bus (EventBus): The event bus used for event handling.
        """
        self.action_queue = []
        event_bus.subscribe("ATTACK", self)
        event_bus.subscribe("DEFEND", self)

    def handle_event(self, event):
        """
        Handles the events received from the event bus.

        Args:
            event (Event): The event to be handled.
        """
        if event.type == "ATTACK":
            self.queue_action("attack")
        elif event.type == "DEFEND":
            self.queue_action("defend")

    def queue_action(self, action_type, target=None):
        """
        Adds an action to the action queue.

        Args:
            action_type (str): The type of action to be queued.
            target (Entity, optional): The target entity for the action. Defaults to None.
        """
        self.action_queue.append(ActionComponent(action_type, target))

    def update(self, world: World):
        """
        Updates the battle system based on the current state of the world.

        Args:
            world (World): The World object in which the battle system operates.
        """
        # Process the action queue and perform actions
        pass