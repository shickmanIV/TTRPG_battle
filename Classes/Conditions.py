from abc import ABC, abstractmethod
from Game.Actor import Actor
import logging # Run with "--log=INFO"

class Condition():
    def __init__(self, name: str, desc: str, effects=None):
        self.name = name
        self.desc = desc
        self.effects = effects or []
    
    # Adds an effect by passing a lambda expression to this condition
    def addEffect(self, newEffect=None):
        self.effects.append(newEffect)

    def apply(self, target: Actor):
        logging.info(f"Applying Condition {self.name} to Actor {target.name}")
        for modify in self.effects:
            modify(target)
        return
    

        