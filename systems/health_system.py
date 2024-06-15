from systems.system import System
from components.health_component import HealthComponent
import logging # Run with "--log=INFO"

logger = logging.getLogger(__name__)

class HealthSystem(System):
    """
    A system responsible for updating the health of entities in the game.

    Args:
        event_bus (EventBus): The event bus used for publishing events.

    Attributes:
        event_bus (EventBus): The event bus used for publishing events.
    """

    def __init__(self, event_bus):
        self.event_bus = event_bus

    def update(self, entity_manager):
        """
        Update the health of all entities with a HealthComponent.

        Args:
            entity_manager (EntityManager): The entity manager containing all entities.

        Returns:
            None
        """
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
        """
        Check if an entity dies instantly.

        An entity dies instantly if its current HP is reduced below 0 by a value greater than or equal to its maximum HP.
        Otherwise, the entity's HP is simply reset to 0.

        Args:
            health_component (HealthComponent): The health component of the entity.

        Returns:
            bool: True if the entity dies instantly, False otherwise.
        """
        if health_component.current_hp < 0:
            if abs(health_component.current_hp) >= health_component.max_hp:
                return True
            else:
                health_component.current_hp = 0
        return False