from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    _cargo: float = 0
    _max_cargo: float
    def __init__(self, max_cargo):
        super().__init__()
        self._max_cargo = max_cargo

    def load_cargo(self, cargo):
        res_cargo = self._cargo + cargo
        if res_cargo > self._max_cargo:
            raise CargoOverload(f'Максимальный вес: {self._max_cargo}, вес после добавления {cargo}: {res_cargo}')
        self._cargo = res_cargo

    def remove_all_cargo(self):
        cargo = self._cargo
        self._cargo = 0
        return cargo
