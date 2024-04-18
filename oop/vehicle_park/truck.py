from vehicle import Vehicle



class Truck(Vehicle):

    def __init__(self, mileage: float = 0.0, licence_plate: str = '', fuel_type: str = '',
                 fuel_consumption: float = 0.0, fixed_cost: float = 0.0, inspection: object = None,
                 insurance: object = None, driver_status: object = None, trailer_capability: object = None,
                 load_capacity: int = 30, trailer_capacity: int = 5
                 ):

        super().__init__(mileage, licence_plate, fuel_type, fuel_consumption, fixed_cost, inspection, insurance,
                         driver_status)

        self.trailer_capability = trailer_capability
        self.load_capacity = load_capacity
        self.trailer_capacity = trailer_capacity

    def how_many_trucks_and_trailers(self, total_load,):
        from math import ceil
        number_of_trucks = ceil(total_load / (self.load_capacity + self.trailer_capacity))
        number_of_trailers = ceil((total_load - self.load_capacity * number_of_trucks) / self.trailer_capacity)
        if number_of_trailers <=0:
            return (f"Reikia {number_of_trucks} ir 0 priekabu ")
        else:
            return (f"Reikia {number_of_trucks} sunkvezimiu ir {number_of_trailers} priekabu ")