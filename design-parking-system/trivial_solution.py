# This is a generic file for the trivial solution
from enum import Enum

class Size(Enum):
    BIG = 0
    MEDIUM = 1
    SMALL = 2


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.parking_lot = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        match carType:
            case 1:
                return self.update_parking_lot_place_if_exists(carType_index=Size.BIG.value)

            case 2:
                return self.update_parking_lot_place_if_exists(carType_index=Size.MEDIUM.value)

            case 3:
                return self.update_parking_lot_place_if_exists(carType_index=Size.SMALL.value)
            case _:
                raise TypeError("No such Type")

    def update_parking_lot_place_if_exists(self, carType_index):
        if self.parking_lot[carType_index] > 0:
            self.parking_lot[carType_index] -= 1
            return True
        else:
            return False


if __name__ == '__main__':
    solution_input = []
    obj = ParkingSystem(big=1, medium=1, small=0)
    param_1 = obj.addCar(1)
    param_2 = obj.addCar(2)
    param_3 = obj.addCar(3)
    param_4 = obj.addCar(1)
