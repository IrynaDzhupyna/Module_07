from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory



def test_factory(factory: CreatureFactory, message) -> None:
    print(message)
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print()


def main() -> None:
    heal_factory = HealingCreatureFactory()
    test_factory(heal_factory, "Testing Creature with healing capability")


if __name__ == "__main__":
    main()