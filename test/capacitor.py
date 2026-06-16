from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory



def test_factory(factory: CreatureFactory, c_type: str) -> None:
    print(f"Testing Creture with {c_type} capability")
    base = factory.create_base()
    evolved = factory.create_evolved()
    stage: list = [base, evolved]

    for element in stage:
        if element == base:
            print(" base:")
        elif element == evolved:
            print(" evolved:")
        print(element.describe())
        print(element.attack())
        
        if c_type == "healing":
            print(element.heal())
        elif c_type == "transform":
            print(element.transform())
            print(element.attack())
            print(element.revert())


def main() -> None:
    heal_factory = HealingCreatureFactory()
    test_factory(heal_factory, "healing")
    print()
    transform = TransformCreatureFactory()
    test_factory(transform, "transform")


if __name__ == "__main__":
    main()