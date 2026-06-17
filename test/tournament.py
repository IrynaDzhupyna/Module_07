from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggresiveStrategy, DefensiveStrategy


def battle(opponents: list[tuple]) -> None:
    # print(some info)
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_1, strategy_1 = opponents[i]
            factory_2, strategy_2 = opponents[j]
            creature_1 = factory_1.create_base()
            creature_2 = factory_2.create_base()
    print("* Battle *")
    print(f"{creature_1.describe()}\n vs\n{creature_2.describe()}")
    print(" now fight!")
    print(creature_1.attack())
    print(creature_2.attack())
    



def main() -> None:
    # players
    """lameling = FlameFactory().create_base()
    aqua = AquaFactory()
    Aquabub = AquaFactory.create_base()
    Healing = HealingCreatureFactory.create_base()
    shiftling = TransformCreatureFactory().create_base()

    # strategies
    Normal = NormalStrategy()
    aggresive = AggresiveStrategy()
    Defensive = DefensiveStrategy()"""

    print("Tournament 0 (basic)")
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    battle(opponents)





if __name__ == "__main__":
    main()