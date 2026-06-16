from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self):
        pass