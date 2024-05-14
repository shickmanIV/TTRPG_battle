from enum import Enum

class Spell:
    name: str
    school: int
    castingtime = None
    range = []
    description = ""

    def __init__(self, name="", school="", castTime = None, range = None, description = "description"):
        self.name = name
        self.school = school
        self.castingtime = castTime
        self.range = range
        self.description = description

    def print(self):
        print(self.name)
        print(self.school)
        print(self.castingtime)
        print(self.range)
        print(self.description)
