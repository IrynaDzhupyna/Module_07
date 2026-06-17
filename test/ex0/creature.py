from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name=None, c_type=None) -> None:
        self.name = name
        self.c_type = c_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.c_type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", c_type="Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", c_type="Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", c_type="Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", c_type="Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
