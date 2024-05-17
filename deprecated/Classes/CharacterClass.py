from Classes.Constants import AbilityType
from Classes.Proficiency import Proficiency

class DnDClass:

    name: str
    hit_die: int
    multiclass_req: tuple[AbilityType, int]
    proficiencies: set[Proficiency]
    
    def __init__(self, name: str, hit_die: int):
        self.name = name
        self.hit_die = hit_die
    
    def __init__(self, form_data: dict):
        self.name = "formname"
        self.hit_die = -1

    def __str__(self):
        return "Class:\n\tname: %s\n\thit_die: %s" % (self.name, self.hit_die)

    