from vehicle import Vehicle
from datetime import datetime

class Car(Vehicle):

    def __init__(self, mileage: float = 0.0, licence_plate: str = '', fuel_type: str = '',
                 fuel_consumption: float = 0.0, fixed_cost: float = 0.0, inspection: object = None,
                 insurance: object = None, driver_status: object = None):
        super().__init__(mileage, licence_plate, fuel_type, fuel_consumption, fixed_cost, inspection, insurance,
                         driver_status)
