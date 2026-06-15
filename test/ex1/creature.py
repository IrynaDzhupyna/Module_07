from .capability import HealCapability, TransformCapability
from ex0.creature import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Sproutling", c_type="Grass")

    def heal(self, target) -> str:
        return f"{self.name} heals itself for a small amount"
    
    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"
    

class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Boomelle", c_type="Grass/Fairy")

    def heal(self, target) -> str:
        return f"{self.name} heals itself and others for a large amount"
    
    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__(name="Shiftling", c_type="Normal")
        self.transformed = False
    
    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        return f"{self.name} returns to normal."
    
    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} performes a boosted strike!"
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__(name="Morphagon", c_type="Normal/Dragon")
        self.transformed = False

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        return f"{self.name} stabilizes its form."
    
    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."