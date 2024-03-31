from order import Order
from vehicle import *
import os
import csv

class OrderRepository:
    def __init__(self, filename: str) -> None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.__filename = os.path.join(script_dir, filename)
    
    def save_orders(self, orders: list[Order]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            for order in orders:
                writer.writerow(order.convert_to_list())
    
    
    def create_vehicle_and_package(self,row):
        vehicle_type = row[2]
        if vehicle_type == "Sedan":
            model, color, model_year, num_seats = row[3], row[5], int(row[6]), int(row[7])
            vehicle = Sedan(model, color, model_year, num_seats)
        elif vehicle_type == "SUV":
            model, color, model_year, roof_rack_type = row[3], row[5], int(row[6]), row[7]
            vehicle = SUV(model, color, model_year, roof_rack_type)
        elif vehicle_type == "Truck":
            model, color, model_year, cargo_bed_size = row[3], row[5], int(row[6]), row[7]
            vehicle = Truck(model, color, model_year, cargo_bed_size)
        elif vehicle_type == "Minivan":
            model, color, model_year = row[3], row[5], int(row[6])
            sliding_doors, towing_capacity = row[7], int(row[8])
            vehicle = Minivan(model, color, model_year, sliding_doors, towing_capacity)
        
        package = Feature_Package()
        for i in range(8, len(row)):
            feature = row[i]
            if feature.lower() == "enhanced safety features":
                package.add_optional_feature(EnhancedSafetyFeatures())
            elif feature.lower() == "security":
                package.add_optional_feature(Security())
            elif feature.lower() == "entertainment system":
                package.add_optional_feature(EntertainmentSystem())
            elif feature.lower() == "sunroof":
                package.add_optional_feature(Sunroof())
        
        return vehicle, package

    def read_orders(self) -> list[Order]:
        orders: list[Order] = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                customer_name, customer_id, vehicle_type = row[0], row[1], row[2]
                vehicle, package = self.create_vehicle_and_package(row)
                orders.append(Order(customer_name, customer_id, vehicle, package))
        return orders



def main():
    orders =[]
    sedan1 = Sedan("Toyota Camry", "Blue", 2023, 5)
    feature1 = EnhancedSafetyFeatures()
    feature2= Security()
    package1 = Feature_Package()
    package1.add_optional_feature(feature1)
    package1.add_optional_feature(feature2)
    orders.append(Order("John Doe", "123456",sedan1, package1 ))

    repository = OrderRepository("orders.csv")
    repository.save_orders(orders)

    orders2 = repository.read_orders()
    for order in orders2:
        print(order)

if __name__ == "__main__":
    main()


