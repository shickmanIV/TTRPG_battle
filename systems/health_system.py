from systems.system import System
from components.health_component import HealthComponent

# Really just an example for reference
class HealthSystem(System):
    def update(self, entity_manager):
        for entity in entity_manager.get_all_entities_with_component(HealthComponent):
            health_component = entity.get_component(HealthComponent)
            # Perform health-related updates
            if health_component.current_health <= 0:
                print(f"Entity {entity.entity_id} has fainted.")