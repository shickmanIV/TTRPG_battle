from entities.entity import Entity
from entities.actor import Actor

def grog() -> Entity:
    grog = Actor('grog', name="Grog", max_hp=12, str=14, con=16, dex=9, int=6, wis=11, cha=9)
    return grog