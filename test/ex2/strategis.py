from abc import ABC, abstractmethod
from ex1.capability import HealCapability, TransformCapability
from ex0.creature import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    '''
    any creature
    '''
    def act(self) -> str:
        pass

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggresiveStrategy(BattleStrategy):
    ''' with transform capabilities
    '''
    def act(self) -> str:
        pass

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False
    

class DefensiveStrategy(BattleStrategy):
    '''
    healing capability
    '''
    def act(self) -> str:
        pass

    def is_valid(self, creature):
        if isinstance(creature, HealCapability):
            return True
        return False
