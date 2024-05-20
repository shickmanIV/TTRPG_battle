from components.health_component import HealthComponent
from components.bio_component import BioComponent
from entities.entity import Entity
from entities.entity_manager import EntityManager

def grog(entity_manager: EntityManager) -> Entity:
    grog = entity_manager.create_entity('grog')
    grog.add_component(HealthComponent(12))
    grog.add_component(BioComponent("Grog"))

    return grog