from ex0.factory import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory):
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print()

def main() -> None:
    factory = FlameFactory()
    test_factory(factory)

    factory = AquaFactory()
    test_factory(factory)


if __name__ == "__main__":
    main()