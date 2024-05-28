from entities.entity_manager import EntityManager
import heapq

class World(EntityManager):
    def __init__(self):
        self.__systems = []
        super().__init__()

    def add_system(self, system, priority=0):
        # Use a tuple of (priority, system) when adding to the queue
        heapq.heappush(self.__systems, (priority, system))
        return system
    
    def get_system(self, system_type):
        for _, system in self.__systems:
            if isinstance(system, system_type):
                return system
        return None

    def update(self):
        # Systems are updated in order of their priority
        for _, system in sorted(self.__systems):
            system.update(self)