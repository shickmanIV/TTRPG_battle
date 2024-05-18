from components.component import Component

# Really just an example for reference
class HealthComponent(Component):
    def __init__(self, max_hp):
        self.current_hp = max_hp
        self.max_hp = max_hp
        self.temporary_hp = 0

    def print_attributes(self, indent=""):
        print(indent + "current_hp:", self.current_hp)
        print(indent + "max_hp:", self.max_hp)
        print(indent + "temporary_hp:", self.temporary_hp)
