from entities.entity import Entity
from components.health_component import HealthComponent
from components.ability_score_component import AbilityScores

# A subclass of Entity representing an actor in the combat simulation
class Actor(Entity):
    def __init__(self, entity_id, **args):
        super().__init__(entity_id)

        self.add_component(HealthComponent(args.get('max_hp', 1)))
        self.add_component(AbilityScores(**args))

        self.character_name = args.get('character_name')
        self.character_class = args.get('character_class')
        self.level = args.get('level') or 1
        self.background = args.get('background')
        self.player_name = args.get('player_name')
        self.race = args.get('race')
        self.allignment = args.get('allignment')
        self.experience_points: int = args.get('experience_points')

        self.age: tuple[int, str] = None
        self.height: tuple[int, str] = None
        self.weight: tuple[int, str] = None
        self.eyes: str = ""
        self.skin: str = ""
        self.hair: str = ""

