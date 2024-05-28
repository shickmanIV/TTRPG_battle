from systems.system import System
from event import Event

class InputSystem(System):
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def capture_input(self, user_input):
        event_type = self.translate_input_to_event(user_input)
        event = Event(event_type)
        self.event_bus.publish(event)

    def translate_input_to_event(self, user_input):
        # Translate the raw user_input into an event type
        # For simplicity, we'll assume that the user_input is already a valid event type
        return user_input

    def update(self, world):
        # This system doesn't need to do anything on update
        pass