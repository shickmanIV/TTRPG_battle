from game_loop import GameLoop
from components.health_component import HealthComponent
from components.bio_component import BioComponent

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
                     
def test3():
    game = GameLoop()
    ed = game.entity_manager.create_entity('bob')
    
    # same as: game.entity_manager.get_entity('bob').add_component(HealthComponent(12)) 
    ed.add_component(HealthComponent(12))
    ed.add_component(BioComponent("Bob"))
    
    game.entity_manager.print_all_entities()
