from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    print("Testing battle")
    base_1 = factory_1.create_base()
    base_2 = factory_2.create_base()
    print(f"{base_1.describe()}\n vs.\n{base_2.describe()}\n fight!")
    print(base_1.attack())
    print(base_2.attack())


def main() -> None:
    factory_1 = FlameFactory()
    test_factory(factory_1)

    factory_2 = AquaFactory()
    test_factory(factory_2)
    battle(factory_1, factory_2)


if __name__ == "__main__":
    main()
