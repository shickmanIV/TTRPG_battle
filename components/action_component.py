import logging

logger = logging.getLogger(__name__)
valid_types = {'ACTION', 'BONUS', 'REACTION', 'FREE'}

# A class for representing a specific action taken by a player
class ActionComponent:
    def __init__(self, action_type, target=None):
        if action_type not in valid_types:
            logger.warning(f"Invalid Action Type: '{action_type}'")
        self.action_type = action_type
        self.target = target
