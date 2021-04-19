# using dictionary
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {
            'big' : big,
            'medium' : medium,
            'small' : small
        }
        
    def addCar(self, carType: int) -> bool:
        types = {
            1 : 'big',
            2 : 'medium',
            3 : 'small'
        }
        
        if self.spaces[types[carType]] == 0:
            return False
        else:
            self.spaces[types[carType]] -= 1
            return True
        

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)