from order import *
from vehicle import *
import os
import csv

class VehicleRepository:
    def __init__(self, filename: str) -> None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.__filename = os.path.join(script_dir, filename)
    
    def save_vehicles(self, vehicles: list[Vehicle]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            for vehicle in vehicles:
                if isinstance(vehicle, Sedan):
                    row = ["Sedan", vehicle.model, vehicle.base_price, vehicle.color, vehicle.model_year, vehicle.num_seats]
                elif isinstance(vehicle, Truck):
                    row = ["Truck", vehicle.model, vehicle.base_price, vehicle.color, vehicle.model_year, vehicle.cargo_bed_size]
                elif isinstance(vehicle, SUV):
                    row = ["SUV", vehicle.model, vehicle.base_price, vehicle.color, vehicle.model_year, vehicle.roof_rack_type]
                elif isinstance(vehicle, Minivan):
                    row = ["Minivan", vehicle.model, vehicle.base_price, vehicle.color, vehicle.model_year, vehicle.sliding_doors, vehicle.towing_capacity]
                writer.writerow(row)

    def read_vehicles(self) -> list[Vehicle]:
        vehicles:list[Vehicle] = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                vehicle_type = row[0]
                if vehicle_type == "Sedan":
                    model, color, model_year, num_seats = row[1], row[3], row[4], row[5]
                    vehicle = Sedan(model, color, int(model_year), int(num_seats))
                elif vehicle_type == "Truck":
                    model, color, model_year, cargo_bed_size = row[1], row[3], row[4], row[5]
                    vehicle = Truck(model, color, int(model_year), cargo_bed_size)
                elif vehicle_type == "SUV":
                    model,  color, model_year, roof_rack_type = row[1], row[3], row[4], row[5]
                    vehicle = SUV(model, color, int(model_year), roof_rack_type)
                elif vehicle_type == "Minivan":
                    model, color, model_year, sliding_doors, towing_capacity = row[1], row[3], row[4], row[5], row[6]
                    vehicle = Minivan(model, color, int(model_year), sliding_doors, int(towing_capacity))
                vehicles.append(vehicle)
        return vehicles

def main():
    vehicles = [
        Sedan("Toyota Camry", "Blue", 2023, 5),
        Truck("Ford F150", "Black", 2022, "Short Bed"),
        SUV("Honda CR-V", "Red", 2023, "Crossbar"),
        Minivan("Chrysler Pacifica", "White", 2024, True, 3500)
    ]
    
    repo = VehicleRepository("vehicles.csv")
    repo.save_vehicles(vehicles)

    loaded_vehicles = repo.read_vehicles()
    for vehicle in loaded_vehicles:
        print(vehicle)

if __name__ == "__main__":
    main()
