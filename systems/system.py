from abc import ABC, abstractmethod

class System(ABC):
    @abstractmethod
    def update(self, entity_manager):
        pass
    
    def handle_event(self, event):
        pass