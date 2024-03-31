from order import Order
from vehicle import *
from vehiclerepo import *
from orderrepose import *

class Dealership:
    def __init__(self,name:str,address:str) -> None:
        self.__name = name
        self.__address = address
        self.__inventory:list[Vehicle]=[]
        self.__orders:list[Order]=[]

    def add_vehicle(self, vehicle:Vehicle):
        if vehicle not in self.__inventory:
            self.__inventory.append(vehicle)
            self.save_order_to_vehicledb()
        else:
            print("Vehicle already exist")
    
    def add_vehicle_to_order(self, order: Order):
        found = False
        for vehicle in self.__inventory:
            if isinstance(vehicle, Sedan):
                if (vehicle.model.lower() == order.vehicle.model.lower() and 
                    vehicle.color.lower() == order.vehicle.color.lower() and 
                    vehicle.model_year == order.vehicle.model_year and 
                    vehicle.base_price == order.vehicle.base_price and 
                    vehicle.num_seats == order.vehicle.num_seats):
                    self.__orders.append(order)
                    self.save_order_to_orderdb()
                    found = True
                    break
            elif isinstance(vehicle, Truck):
                if (vehicle.model.lower() == order.vehicle.model.lower() and 
                    vehicle.color.lower() == order.vehicle.color.lower() and 
                    vehicle.model_year == order.vehicle.model_year and 
                    vehicle.base_price == order.vehicle.base_price and 
                    vehicle.cargo_bed_size == order.vehicle.cargo_bed_size):
                    self.__orders.append(order)
                    self.save_order_to_orderdb()
                    found = True
                    break
            elif isinstance(vehicle, SUV):
                if (vehicle.model.lower() == order.vehicle.model.lower() and 
                    vehicle.color.lower() == order.vehicle.color.lower() and 
                    vehicle.model_year == order.vehicle.model_year and 
                    vehicle.base_price == order.vehicle.base_price and 
                    vehicle.roof_rack_type == order.vehicle.roof_rack_type):
                    self.__orders.append(order)
                    self.save_order_to_orderdb()
                    found = True
                    break
            elif isinstance(vehicle, Minivan):
                if (vehicle.model.lower() == order.vehicle.model.lower() and 
                    vehicle.color.lower() == order.vehicle.color.lower() and 
                    vehicle.model_year == order.vehicle.model_year and 
                    vehicle.base_price == order.vehicle.base_price and 
                    vehicle.sliding_doors == order.vehicle.sliding_doors and 
                    vehicle.towing_capacity == order.vehicle.towing_capacity):
                    self.__orders.append(order)
                    self.save_order_to_orderdb()
                    found = True
                    break
        return found

    def search_by_feature(self, feature: OptionalFeature):
        self.get_orders_from_orderdb()
        matching_vehicles:list[Vehicle] = []
        for order in self.__orders:
            for fea in order.feature_package:
                if fea.name == feature.name and fea.price == feature.price:
                    matching_vehicles.append(order)
        return matching_vehicles

    def remove_vehicle_from_inventory(self, vehicle: Vehicle):
        self.get_orders_from_orderdb()
        if vehicle in self.__inventory:
            self.__inventory.remove(vehicle)
            self.save_order_to_vehicledb()
            for order in self.__orders:
                if order.vehicle.model == vehicle.model and order.vehicle.base_price == vehicle.base_price:
                    self.remove_vehicle_from_order(order.customer_name,order.order_id)
            
    def remove_vehicle_from_order(self, name:str,orderid:str):
        for order in self.__orders.copy():
            if order.customer_name == name and orderid == order.order_id:
                self.__orders.remove(order)
                self.save_order_to_orderdb()
    
    def view_order(self):
        self.get_orders_from_orderdb()
        return self.__orders
    
    def view_vehicle(self):
        self.get_vehicle_from_vehicledb()
        if len(self.__inventory)==0:
            return None
        return self.__inventory

    def highest_and_lowest_price(self):
        self.get_vehicle_from_vehicledb()
        max: Vehicle= self.__inventory[0]
        min: Vehicle = self.__inventory[0]
        if not self.__inventory:
            return None,None
        for vehicle in self.__inventory:
            if vehicle.base_price > max.base_price:
                max = vehicle
            elif vehicle.base_price < min.base_price:
                min =vehicle
        return max,min

    def search_price(self,price:float):
        self.get_vehicle_from_vehicledb()
        vehicle_price=[]
        for vehicle in self.__inventory:
            if vehicle.base_price == price:
                vehicle_price.append(vehicle)
        return vehicle_price
    
    def __str__(self) -> str:
        outputinventory =''
        outputorder=''
        for vehicle in self.__inventory:
            outputinventory+= str(vehicle)
        for order in self.__orders:
            outputorder += str(order)
        return f'Name:{self.__name}\nAddress:{self.__address}\nInventory: {outputinventory}\nOrders: {outputorder}'
    
    def __repr__(self) -> str:
        return str(self)

    def get_vehicle_from_vehicledb(self):
        repos = VehicleRepository("vehicles.csv")
        self.__inventory = repos.read_vehicles()
    
    def get_orders_from_orderdb(self):
        repos = OrderRepository("orders.csv")
        self.__orders = repos.read_orders()
    
    def save_order_to_vehicledb(self):
        repos = VehicleRepository("vehicles.csv")
        repos.save_vehicles(self.__inventory)

    def save_order_to_orderdb(self):
        repos = OrderRepository("orders.csv")
        repos.save_orders(self.__orders)


def main():
    # Create a dealership
    dealership = Dealership("My Dealership", "123 Main Street")

    #ONLY DEALER CAN DO THIS
    # Add vehicles to the inventory
    sedan1 = Sedan("Toyota Camry", "Blue", 2023, 5)
    sedan2 = Sedan("Honda Accord", "Red", 2022, 5)
    suv1 = SUV("Ford Explorer", "White", 2023, 'standard')

    dealership.add_vehicle(sedan1)
    dealership.add_vehicle(sedan2)
    dealership.add_vehicle(suv1)


    # Test remove_vehicle_from_inventory function
    dealership.remove_vehicle_from_inventory(sedan2)

if __name__ == "__main__":
    main()







        
