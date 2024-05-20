from entities.entity import Entity
from components.health_component import HealthComponent

# A subclass of Entity representing an actor in the combat simulation
class Actor(Entity):
    def __init__(self, entity_id, name="", max_hp=1):
        super().__init__(entity_id)
        self.add_component(HealthComponent(max_hp))

        self.character_name = name

        self.character_class = None
        self.level = 1
        self.background = None
        self.player_name = None
        self.race = None
        self.allignment = None
        self.experience_points: int = None

        self.age: tuple[int, str] = None
        self.height: tuple[int, str] = None
        self.weight: tuple[int, str] = None
        self.eyes: str = ""
        self.skin: str = ""
        self.hair: str = ""

