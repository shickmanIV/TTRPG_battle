from abc import ABC, abstractmethod

class Condition():
    def __init__(self, name: str, desc: str, effects=None):
        self.name = name
        self.desc = desc
        self.effects = effects or []

        