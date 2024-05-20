from components.health_component import HealthComponent
from components.bio_component import BioComponent
from entities.entity import Entity

def grog() -> Entity:
    grog = Entity('grog')
    grog.add_component(HealthComponent(12))
    grog.add_component(BioComponent("Grog"))
    return grog