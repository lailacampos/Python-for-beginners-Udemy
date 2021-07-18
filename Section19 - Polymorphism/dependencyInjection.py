# Dependency Injection

# Classes often require references to other classes. For example, a Car class might need a reference to an Engine
# class. These required classes are called dependencies, and in this example the Car class is dependent on having an
# instance of the Engine class to run.

class Flight:
    def __init__(self, engine):
        self.engine = engine  # <= Dependency injection

    def startEngine(self):
        self.engine.start()


class AirbusEngine:
    def start(self):
        print('Starting AirBus engine')


class BoingEngine:
    def start(self):
        print('Starting Boing engine')


airbus_engine = AirbusEngine()
flight = Flight(airbus_engine)
flight.startEngine()

boing_engine = BoingEngine()
flight2 = Flight(boing_engine)
flight2.startEngine()
