from components.health_component import HealthComponent
from entities.entity import Entity
from entities.actor import Actor

def grog() -> Entity:
    grog = Actor('grog', name="Grog", max_hp=12)
    return grog