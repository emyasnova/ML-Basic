from homework_05.base import Vehicle
from homework_05.engine import Engine

class Car(Vehicle):
    _engine: Engine

    def set_engine(self, engine: Engine):
        self._engine = engine
