from homework_05.exceptions import LowFuelError, NotEnoughFuel

from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight = 1000, fuel = 500, fuel_consumption = 100):
        self._weight = weight
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption
        self._started = False

    def start(self):
        if self._started:
            return
        if self._fuel <= 0:
            raise LowFuelError()
        self._started = True

    def move(self, distance):
        req_fuel = distance * self._fuel_consumption
        if self._fuel < req_fuel:
            raise NotEnoughFuel
        self._fuel -= req_fuel