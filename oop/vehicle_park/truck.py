from vehicle import Vehicle


class Truck(Vehicle):

    def __init__(self, mileage: float = 0.0, licence_plate: str = '', fuel_type: str = '',
                 fuel_consumption: float = 0.0, fixed_cost: float = 0.0, inspection: object = None,
                 insurance: object = None, driver_status: object = None, trailer_capability: object = None,
                 load_capacity: int = 30, trailer_capacity: int = 5):

        super().__init__(mileage, licence_plate, fuel_type, fuel_consumption, fixed_cost, inspection, insurance,
                         driver_status)

        self.trailer_capability = trailer_capability
        self.load_capacity = load_capacity
        self.trailer_capacity = trailer_capacity

    #def can_driver_get_trailer(self):
        #from driver import driver_one
        #if driver_one() ==


