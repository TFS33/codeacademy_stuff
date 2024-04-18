from datetime import datetime
from vehicle import Vehicle
import math


class Bus(Vehicle):
    def __init__(self, mileage: float = 0.0, licence_plate: str = '', fuel_type: str = '',
                 fuel_consumption: float = 0.0, fixed_cost: float = 0.0, inspection: object = None,
                 insurance: object = None, driver_status: object = None, number_of_passangers: int = 54):
        super().__init__(mileage, licence_plate, fuel_type, fuel_consumption, fixed_cost, inspection, insurance,
                         driver_status)
        self.number_of_passengers = number_of_passangers

    def get_how_many_buses_needed(self, all_passengers):
        try:
            return math.ceil(all_passengers / self.number_of_passengers)
        except ZeroDivisionError as e:
            print(f"Nera keleiviu ", {e})

    def get_cost_of_transporting(self, fuel_price_diesel,):
        cost_of_fuel = self.mileage / 100 * self.fuel_consumption * fuel_price_diesel
        cost_of_day_maintenance = self.fixed_cost / 365
        total_cost = cost_of_fuel + cost_of_day_maintenance
        return round(total_cost * self.get_how_many_buses_needed(all_passengers= 0), 2)





bus = Bus(
    mileage=10000, licence_plate="TFS456", fuel_type="Diesel", fuel_consumption=10, fixed_cost=500,
    inspection=datetime(2024, 5, 10), insurance=datetime(2025, 10, 10),
    driver_status=True, number_of_passangers=30
)

