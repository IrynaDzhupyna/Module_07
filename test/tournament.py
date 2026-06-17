from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


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

            if strategy_1.is_valid(creature_1) and strategy_2.is_valid(creature_2):
                print(creature_1.attack())
                print(creature_2.attack())
            else:
                print("Battle error, aborting tournament: Invalid Creature '{creature.name}' for this aggresive strategy")


def main() -> None:
    """
    print("Tournament 0 (basic)")
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    battle(opponents)"""

    print("Tournament 1 (error)")
    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle(opponents)





if __name__ == "__main__":
    main()