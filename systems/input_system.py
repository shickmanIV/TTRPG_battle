from systems.system import System
from event import Event

class InputSystem(System):
    """
    A system that captures user input and publishes corresponding events.

    Attributes:
        event_bus (EventBus): The event bus used to publish events.

    Methods:
        capture_input: Captures user input and publishes the corresponding event.
        translate_input_to_event: Translates user input into an event type.
        update: Updates the system (no action needed for InputSystem).
    """

    def __init__(self, event_bus):
        """
        Initializes the InputSystem.

        Args:
            event_bus (EventBus): The event bus used to publish events.
        """
        self.event_bus = event_bus

    def capture_input(self, user_input):
        """
        Captures user input and publishes the corresponding event.

        Args:
            user_input (str): The user input to capture.
        """
        event_type = self.translate_input_to_event(user_input)
        event = Event(event_type)
        self.event_bus.publish(event)

    def translate_input_to_event(self, user_input):
        """
        Translates user input into an event type.

        Args:
            user_input (str): The user input to translate.

        Returns:
            str: The translated event type.
        """
        # Translate the raw user_input into an event type
        # For simplicity, we'll assume that the user_input is already a valid event type
        return user_input

    def update(self, world):
        """
        Updates the system.

        Args:
            world: The game world (not used in InputSystem).
        """
        # This system doesn't need to do anything on update
        pass