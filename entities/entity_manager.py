class EntityManager:
    def __init__(self):
        self.entities = {}

    def add_entity(self, entity):
        self.entities[entity.entity_id] = entity
        return entity
    
    def get_entity(self, entity_id):
        return self.entities.get(entity_id)

    def get_all_entities_with_component(self, component_type):
        return [entity for entity in self.entities.values() if entity.has_component(component_type)]
    
    def print_all_entities(self):
        for id, entity in self.entities.items():
            print(entity.__class__.__name__, id)
            entity.print_components("    ")