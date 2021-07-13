class Flight:
    def __init__(self, engine):
        self.engine = engine

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