from entities.entity_manager import EntityManager

class Entity:
    entity_manager = EntityManager()

    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.components = {}
        self.entity_manager.add_entity(self)

    def add_component(self, component):
        self.components[type(component)] = component

    def get_component(self, component_type):
        return self.components.get(component_type)

    def has_component(self, component_type):
        return component_type in self.components
    
    def print_components(self, indent=""):
        for type, component in self.components.items():
            print(indent + type.__name__)
            component.print_attributes(indent + "    ")