from systems.system import System
from components.health_component import HealthComponent
import logging # Run with "--log=INFO"

logger = logging.getLogger(__name__)

class HealthSystem(System):
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def update(self, entity_manager):
        for entity in entity_manager.get_all_entities_with_component(HealthComponent):
            health_component = entity.get_component(HealthComponent)
            # Perform health-related updates
            if self.instant_death_check(health_component):
                logger.info(f"Entity {entity.entity_id} dies instantly.")
                self.event_bus.publish({"type": "entity_death", "entity": entity})
            elif health_component.current_hp == 0:
                logger.info(f"Entity {entity.entity_id} is unconscious.")
                self.event_bus.publish({"type": "entity_unconscious", "entity": entity})

    def instant_death_check(self, health_component: HealthComponent):
        if health_component.current_hp < 0:
            if abs(health_component.current_hp) >= health_component.max_hp:
                return True
            else:
                health_component.current_hp = 0
        return False