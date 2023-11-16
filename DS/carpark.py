class CarPark:
    def __init__(self):
        self.total_cars = 0
        self.total_cash = 0.0
    
    def payingCar(self):
        self.total_cars += 1
        self.total_cash += 0.50
    
    def nopayCar(self):
        self.total_cars += 1
    
    def displayStats(self):
        print(f"Total cash collected: ${self.total_cash}")
        print(f"Total cars parked: {self.total_cars}")

# Creating an instance of CarPark
car_park = CarPark()

# Simulating car entries
car_park.payingCar()
car_park.nopayCar()
car_park.payingCar()

# Displaying final statistics
car_park.displayStats()
