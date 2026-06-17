from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggresiveStrategy, DefensiveStrategy


def battle(opponents: list[tuple]) -> None:
    print(f" {opponents}")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")
    print("* Battle *")


def main() -> None:
    # players
    Flameling = FlameFactory().create_base()
    aqua = AquaFactory()
    base = aqua.create_base()
    # Aquabub = AquaFactory.create_base()
    Healing = HealingCreatureFactory.create_base()
    shiftling = TransformCreatureFactory().create_base()

    # strategies
    Normal = NormalStrategy()
    aggresive = AggresiveStrategy()
    Defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle([(Flameling, Normal), (Healing, Defensive)])





if __name__ == "__main__":
    main()