from game_loop import GameLoop
from components.health_component import HealthComponent

if __name__ == "__main__":
    game = GameLoop()
    ed = game.entity_manager.create_entity('edward')
    ed.add_component(HealthComponent(11))
    game.display_all_entities()