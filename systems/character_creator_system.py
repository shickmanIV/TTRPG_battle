from entities.actor import Actor
import entities.presets.characters as characters
import logging

logger = logging.getLogger(__name__)

class CharacterCreatorSystem:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def create_character_from_scratch(self):
        actor = Actor()
        self.event_bus.publish("entity_created", actor)
        return actor
    
    def create_character_from_preset(self, preset_name=''):
        # Get a list of all non private/special functions in the characters module
        public_functions = [f for f in dir(characters) if not f.startswith('_')]
        # Print the list of functions for the user to choose from
        print("Available presets:", ('\n\t' + function for function in public_functions))
        # Ask the user to select a function
        target = input("Enter the preset to start from: ")
        # Get the selected function
        preset_function = getattr(characters, target, None)
        if preset_function is not None and callable(preset_function):
            actor = preset_function()
            self.event_bus.publish("entity_created", actor)
        else:
            logger.error(f"Could not find a preset named {target}")