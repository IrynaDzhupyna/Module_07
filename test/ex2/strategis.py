from abc import ABC, abstractmethod
from ex1.capability import HealCapability, TransformCapability
from ex0.creature import Creature
from .exceptions import BattleError


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    '''
    any creature
    '''
    def act(self, creature: Creature) -> str:
        creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    ''' with transform capabilities
    '''
    def act(self, creature: Creature) -> str:
        try:
            self.is_valid(creature)
        except BattleError:
            raise f"Invalid Creature '{creature.name} for this aggresive strategy"
        else:
            creature.transform()
            creature.attack()
            creature.revert()

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False
    

class DefensiveStrategy(BattleStrategy):
    '''
    healing capability
    '''
    def act(self, creature: Creature) -> str:
        try:
            self.is_valid()
        except BattleError:
            raise f"Invalid Creature '{creature.name} for this defensive strategy"
        else:
            creature.attack()
            creature.heal()

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
