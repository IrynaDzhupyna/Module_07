from abc import ABC, abstractmethod
from .creature import Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass



class FlameFactory(CreatureFactory):
    '''
    base = Flameling
    evolved = Pyrodon
    '''
    def create_base(self) -> None:
        return Flameling()

    def create_evolved(self) -> None:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    '''
    base = Aquabub
    evolved = Torragon
    '''
    def create_base(self) -> None:
        return Aquabub()

    def create_evolved(self) -> None:
        return Torragon()
