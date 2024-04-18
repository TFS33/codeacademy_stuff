from datetime import datetime, timedelta
class Vehicle(object):
    def __init__(
        self, mileage: float = 0.0, licence_plate: str = '', fuel_type: str = '',
        fuel_consumption: float = 0.0, fixed_cost: float = 0.0,
        inspection: object = None, insurance: object = None,
        driver_status: object = None
    ):
        self.mileage = mileage
        self.license_plate = licence_plate
        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
        self.fixed_cost = fixed_cost
        self.inspection = inspection
        self.insurance = insurance
        self.driver_status = driver_status

    def get_inspection_status(self):
        if self.inspection:
            if datetime.now() >= self.inspection:
                return f"Transporto priemone numeriais {self.license_plate} turi galiojanti T.A."
            else:
                return f"Sekanti menesi transporto priemonei numeriais {self.license_plate} reikia atlikti T.A. !"
        else:
            return "Nėra nustatyta tikrinimo data."

    def get_insurance_status(self):
        if self.insurance:
            if datetime.now() >= self.insurance:
                return f"Transporto priemone numeriais {self.license_plate} turi galiojanti draudima."
            else:
                return f"Sekanti menesi transporto priemonei numeriais {self.license_plate} reikia atnaujinti draudima.!"
        else:
            return "Nėra nustatyta draudimo data."

    def get_cost_for_distance_driven(self, fuel_price_diesel):
        cost_of_fuel = self.mileage / 100 * self.fuel_consumption * fuel_price_diesel
        cost_of_day_maintenance = self.fixed_cost / 365
        return round(cost_of_fuel + cost_of_day_maintenance, 2)

    def chech_if_driver_is_available(self):
        from main import driver
        curent_time = datetime.now()
        if driver[1] < curent_time < driver[2]:
            print('Vairuotojas atostogauja')
        else:
            print('Vairuotojas gali vaziuoti')


