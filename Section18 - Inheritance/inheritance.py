class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_car(self):
        print('Starting the car')

    def stop_car(self):
        print('Stopping the car')


class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        # The first line is to invoke the parent class's constructor
        BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def diplay_cruiseControl(self):
        print(self.cruiseControlEnabled)

    # Overriding the parent's function
    def start_car(self):
        print('Starting the car')


class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        # The super function invokes the parent class, therefore the self parameter is not needed anymore
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


threeSeries = ThreeSeries(True, 'BMW', '328i', '2018')
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start_car()
threeSeries.stop_car()
threeSeries.diplay_cruiseControl()
