from game_loop import GameLoop
from components.health_component import HealthComponent
from entities.entity import Entity
from entities.actor import Actor
import entities.presets.characters

# For world_test()
from world import World
from systems.input_system import InputSystem
from systems.battle_system import BattleSystem

# Experiments with different ways to access entity attributes
def test():
    game = GameLoop()
    ed = game.entity_manager.create_entity('bob')
    game.entity_manager.get_entity('bob').add_component(HealthComponent(11))

    print()
    print("________________________________________________")
    print("game.entity_manager.get_entity('bob').__dict__")
    print()
    print(game.entity_manager.get_entity('bob').__dict__)
    print("________________________________________________")
    print()

# Experiments with how to print entity and component info legibly
def test2():
    game = GameLoop()
    ed = game.entity_manager.create_entity('bob')
    game.entity_manager.get_entity('bob').add_component(HealthComponent(11))
    ed.add_component(HealthComponent(12))

    for entity_key in game.entity_manager.entities:
        print("________________________________________________")
        print("entity_key:", entity_key)
        print("entities[entity_key]:", game.entity_manager.entities[entity_key])
        print("entities[entity_key].__class__.__name__:", game.entity_manager.entities[entity_key].__class__.__name__)
        print()
        
        for component in game.entity_manager.get_entity(entity_key).components:
            print("\tcomponent.__name__:", component.__name__)
            #print("\tcomponent.current_health:", component.current_health)
            print("\tcomponent.__dict__", component.__dict__)

# Creates some basic entities, then prints all info known about them.               
def test3():
    game = GameLoop()
    bob = Actor('bob', name="Bob", max_hp=12)
    grog = presets.characters.grog()
    game.display_all_entities()
    game.run()

def world_test():
    game = GameLoop()
    bob = game.world.add_entity(Actor('bob', name="Bob", max_hp=12))
    grog = game.world.add_entity(presets.characters.grog())
    game.display_all_entities()
    game.run()