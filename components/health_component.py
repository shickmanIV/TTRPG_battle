from components.component import Component

# Really just an example for reference
class HealthComponent(Component):
    def __init__(self, max_health):
        self.current_health = max_health
        self.max_health = max_health