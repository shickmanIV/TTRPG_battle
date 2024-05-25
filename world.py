from entities.entity_manager import EntityManager

#TODO: Simplify class inheritence
class World(EntityManager):
    def __init__(self):
        self.systems = []
        super().__init__()

    def add_system(self, system):
        self.systems.append(system)
        return system
    
    def get_system(self, system_type):
        for system in self.systems:
            if isinstance(system, system_type):
                return system
        return None

    def update(self):
        for system in self.systems:
            system.update(self)