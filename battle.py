from ex0.factory import FlameFactory


factory = FlameFactory()
base = factory.create_base()
print(base.display())