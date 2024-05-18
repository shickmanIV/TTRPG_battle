
class Entity:
    # In future, possibly initialize with set of components
    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.components = {}

    def add_component(self, component):
        self.components[type(component)] = component

    def get_component(self, component_type):
        return self.components.get(component_type)

    def has_component(self, component_type):
        return component_type in self.components
    
    #
    def print_components(self):
        for component in self.components:
            print(component.__class__.__name__, "\t", component.__dict__)