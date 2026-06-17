from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy)
from ex2 import BattleError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_1, strategy_1 = opponents[i]
            factory_2, strategy_2 = opponents[j]
            creature_1 = factory_1.create_base()
            creature_2 = factory_2.create_base()
            print("\n* Battle *")
            print(f"{creature_1.describe()}\n vs.\n{creature_2.describe()}")
            print(" now fight!")

            try:
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
            except BattleError as e:
                print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_1 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())]
    battle(opponents_1)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_2 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    battle(opponents_2)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents_3 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    battle(opponents_3)


if __name__ == "__main__":
    main()
