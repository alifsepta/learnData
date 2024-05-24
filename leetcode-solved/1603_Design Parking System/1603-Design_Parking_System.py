class ParkingSystem(object):
    def __init__(self, big, medium, small):
        # Initialize the number of available slots for each car type
        self.slots = {1: big, 2: medium, 3: small}

    def addCar(self, carType):
        # Check if there is an available slot for the given carType
        if self.slots[carType] > 0:
            # Decrement the available slots for the given carType
            self.slots[carType] -= 1
            return True
        else:
            return False

# Example usage and testing
parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1)) # return true because there is 1 available slot for a big car
print(parkingSystem.addCar(2)) # return true because there is 1 available slot for a medium car
print(parkingSystem.addCar(3)) # return false because there is no available slot for a small car
print(parkingSystem.addCar(1)) # return false because there is no available slot for a big car. It is already occupied.
