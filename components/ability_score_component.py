from typing import Any
from components.component import Component

class AbilityScores(Component):
    def __init__(self, **args):
        self.scores = {'str': args.get('str', 10),
                       'dex': args.get('dex', 10),
                       'con': args.get('con', 10),
                       'int': args.get('int', 10),
                       'wis': args.get('wis', 10),
                       'cha': args.get('cha', 10)}
        
    def bonus(self, abilitytype) -> int:
        value = self.scores.get(abilitytype)
        return int((value - 10) / 2)
    
    def bonus(self, key: str) -> int:
        value = self.scores[key]
        return int((value - 10) / 2)
    
    def print_attributes(self, indent=""):
        for key, value in self.scores.items():
            bonus = self.bonus(key)
            print(f"{indent}{key}: {value}\t({'+' if (bonus >= 0) else ''}{bonus})")



        
        


    

