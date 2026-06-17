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
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    ''' with transform capabilities
    '''
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise BattleError
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        
        return False
    

class DefensiveStrategy(BattleStrategy):
    '''
    healing capability
    '''
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise BattleError
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
