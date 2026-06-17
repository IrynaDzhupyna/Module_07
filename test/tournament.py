from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2 import BattleError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
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
            
            try:
                # strategies
                strategy_1.act(creature_1)
                # _2.act()
            except BattleError as e:
                raise BattleError (f"Battle error, aborting tournament: {e}")


def main() -> None:
    print("Tournament 0 (basic)")
    opponents_1 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    battle(opponents_1)

    print("Tournament 1 (error)")
    opponents_2 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle(opponents_2)

    print("Tournament 2 (multiple)")
    opponents_3 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    battle(opponents_3)


if __name__ == "__main__":
    main()