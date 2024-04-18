from bus import Bus
from car import Car
from driver import Driver
from truck import Truck
from datetime import datetime

driver = Driver(licence_category='D', holidays_starts= datetime(2024, 5, 10),
                holidays_ends= datetime(2024, 6, 5), salary_per_km=0.12)

truck = Truck(
    mileage=1000.7, licence_plate="KHZ421", fuel_type="Diesel", fuel_consumption=15.2,
    fixed_cost=120.2, inspection=datetime(2025, 10, 6), insurance=datetime(2024, 4, 8),
    driver_status= datetime,  load_capacity=12, trailer_capability=False
)

car = Car(
    mileage=210, licence_plate='NBC878', fuel_consumption=6.8, fuel_type='Diesel', fixed_cost=88,
    inspection=datetime(2025, 11, 2), insurance=datetime(2024, 12, 5)
)
bus = Bus(
    mileage=10000, licence_plate="TFS456", fuel_type="Diesel", fuel_consumption=10, fixed_cost=500,
    inspection=datetime(2024, 5, 10), insurance=datetime(2025, 10, 10),
    driver_status=True, number_of_passangers=30
)

print(driver.can_drive_with_trailer())

print(bus.get_cost_of_transporting(1.56))
print(bus.get_inspection_status())
print(bus.get_cost_for_distance_driven(1.56))
print(bus.get_how_many_buses_needed(400))
print(bus.get_insurance_status())
print(bus.chech_if_driver_is_available())

print(car.get_cost_for_distance_driven(1.56))
print(car.get_inspection_status())
print(car.get_cost_for_distance_driven(120))
print(car.chech_if_driver_is_available())

print(truck.chech_if_driver_is_available())
print(truck.get_cost_for_distance_driven(1.56))
print(truck.get_inspection_status())
print(truck.get_insurance_status())
print(truck.how_many_trucks_and_trailers(120))