from systems.system import System
from components.health_component import HealthComponent
import logging # Run with "--log=INFO"

class HealthSystem(System):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def update(self, entity_manager):
        for entity in entity_manager.get_all_entities_with_component(HealthComponent):
            health_component = entity.get_component(HealthComponent)
            # Perform health-related updates
            if self.instant_death_check(health_component):
                self.logger.info(f"Entity {entity.entity_id} dies instantly.")
            elif health_component.current_hp == 0:
                self.logger.info(f"Entity {entity.entity_id} is unconcious.")

    def instant_death_check(self, health_component: HealthComponent):
        if health_component.current_hp < 0:
            if abs(health_component.current_hp) >= health_component.max_hp:
                return True
            else:
                health_component.current_hp = 0
        return False