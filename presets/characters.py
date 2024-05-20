from components.health_component import HealthComponent
from entities.entity import Entity
from entities.actor import Actor

def grog() -> Entity:
    grog = Actor('grog', "Grog", 12)
    return grog