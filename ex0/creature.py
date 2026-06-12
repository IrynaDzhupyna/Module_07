from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self, message, name, type) -> str:
        return f"{name.capitalize() is a {type.capitalize()} type Creature"


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!!"
        


class Aquabub(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Hydro Gun!"