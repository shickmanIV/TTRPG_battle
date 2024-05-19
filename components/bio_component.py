from components.component import Component

class BioComponent(Component):
    def __init__(self, name=""):

        self.character_name = name
        
        #1st Page
        self.character_class = None
        self.level = None
        self.background = None
        self.player_name = None
        self.race = None
        self.allignment = None
        self.experience_points = None

        #2nd Page
        self.age = ""
        self.height = ""
        self.weight = ""
        self.eyes = ""
        self.skin = ""
        self.hair = ""

    def print_attributes(self, indent=""):  
        print(indent + "character_name:", self.character_name) if self.character_name else None
        print(indent + "character_class:", self.character_class) if self.character_class else None
        print(indent + "level:", self.level) if self.level else None
        print(indent + "background:", self.background) if self.background else None

        print(indent + "player_name:", self.player_name) if self.player_name else None
        print(indent + "race:", self.race) if self.race else None
        print(indent + "allignment:", self.allignment) if self.allignment else None
        print(indent + "experience_points:", self.experience_points) if self.experience_points else None

        print(indent + "age:", self.age) if self.age else None
        print(indent + "height:", self.height) if self.height else None
        print(indent + "weight:", self.weight) if self.weight else None

        print(indent + "eyes:", self.eyes) if self.eyes else None
        print(indent + "skin:", self.skin) if self.skin else None
        print(indent + "hair:", self.hair) if self.hair else None

if __name__ == "__main__":
    bio = BioComponent()
    bio.print_attributes()