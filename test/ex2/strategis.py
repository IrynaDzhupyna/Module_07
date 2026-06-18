from abc import ABC, abstractmethod
from ex1.capability import HealCapability, TransformCapability
from ex0.creature import Creature
from .exceptions import BattleError


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise BattleError(f"Invalid Creature '{creature.name}'"
                              " for this aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise BattleError(f"Invalid Creature '{creature.name}'"
                              " for this defensive strategy")
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
