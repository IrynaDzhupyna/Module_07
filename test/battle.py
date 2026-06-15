from ex0.factory import FlameFactory, AquaFactory


def main() -> None:
    print("Testing factory")
    factory = FlameFactory()
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())

    print("\nTesting Factory")
    factory = AquaFactory()
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


if __name__ == "__main__":
    main()