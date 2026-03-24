class LowFuelError(Exception):
    """Мало топлива"""
    pass

class NotEnoughFuel(Exception):
    """Не хватает топлива"""
    pass

class CargoOverload(Exception):
    """Слишком тяжелый груз"""
    pass
