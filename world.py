from entities.entity_manager import EntityManager
import heapq

class World(EntityManager):
    """
    The World class represents a game world and manages the entities and systems within it.

    It inherits from the EntityManager class, which provides functionality for managing entities.

    Attributes:
        __systems (list): A list of tuples representing the systems in the world, where each tuple contains a priority and a system object.

    Methods:
        add_system(system, priority=0): Adds a system to the world with an optional priority.
        get_system(system_type): Retrieves a system of the specified type from the world.
        update(): Updates all systems in the world in order of their priority.
    """

    def __init__(self):
        """
        Initializes a new instance of the World class.
        """
        self.__systems = []
        super().__init__()

    def add_system(self, system, priority=0):
        """
        Adds a system to the world with an optional priority.

        Args:
            system: The system object to add.
            priority (int, optional): The priority of the system. Systems with higher priority are updated first. Defaults to 0.

        Returns:
            The added system object.
        """
        heapq.heappush(self.__systems, (priority, system))
        return system
    
    def get_system(self, system_type):
        """
        Retrieves a system of the specified type from the world.

        Args:
            system_type: The type of the system to retrieve.

        Returns:
            The system object of the specified type, or None if not found.
        """
        for _, system in self.__systems:
            if isinstance(system, system_type):
                return system
        return None

    def update(self):
        """
        Updates all systems in the world in order of their priority.
        """
        for _, system in sorted(self.__systems):
            system.update(self)