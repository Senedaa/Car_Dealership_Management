from dealership import Dealership
from vehicle import *
from order import Order
import random

class DealershipApp:
    def __init__(self) -> None:
        self.__dealership = Dealership("XYZ","123 Mission Falls")
        self.__dealership.get_orders_from_orderdb()
        self.__dealership.get_vehicle_from_vehicledb()
    
    def show_menu(self):
        print("===== MENU ====")
        print("1. Add Custom Vehicle with desired Option: ")
        print("2. View Order Info and Final Price: ")
        print("3. View Vehicles: ")
        print("4. Search by price: ")
        print("5. Search by Feature(security, sunroof ...)")
        print("6. Search/Check Vehicle with most expensive and least expenisve: ")
        print("7: Remove vehicle from order: ")
        print("8. Exit")
    
    def process_command(self, command) -> bool:
        cont = True 
        if command == 1:
            vehicles = self.__dealership.view_vehicle()
            print("The following vehicles are available")
            if vehicles == None:
                print("Sorry, No vehicle available at this time")
                return
            for vehicle in vehicles:
                print(vehicle)
            name = input("Please enter your name: ")
            order_id= random.randint(1000, 9999)
            print("From the displayed vehicles, please choose the vehicle.")
            base_price = int(input("Please Enter Vehicle Base Price: " ))
            
            if base_price == 30000:
                model = input("Enter the model of the sedan: ")
                color = input("Enter the color of the sedan: ")
                model_year = int(input("Enter the model year of the sedan: "))
                num_seats = int(input("Enter the number of seats for the sedan: "))
                vehicle = Sedan(model, color, model_year, num_seats)
            
            elif base_price == 40000:
                model = input("Enter the model of the SUV: ")
                color = input("Enter the color of the SUV: ")
                model_year = int(input("Enter the model year of the SUV: "))
                roof_rack_type = input("Enter the roof rack type of the SUV: ")
                vehicle = SUV(model, color, model_year, roof_rack_type)
            
            elif base_price == 45000:
                model = input("Enter the model of the minivan: ")
                color = input("Enter the color of the minivan: ")
                model_year = int(input("Enter the model year of the minivan: "))
                sliding_doors = input("Does the minivan have sliding doors? (True/False): ").lower() == 'true'
                towing_capacity = int(input("Enter the towing capacity of the minivan: "))
                vehicle = Minivan(model, color, model_year, sliding_doors, towing_capacity)
            
            elif base_price == 35000:
                model = input("Enter the model of the truck: ")
                color = input("Enter the color of the truck: ")
                model_year = int(input("Enter the model year of the truck: "))
                cargo_bed_size = input("Enter the cargo bed size of the truck: ")
                vehicle = Truck(model, color, model_year, cargo_bed_size)
            
            else:
                print("Invalid vehicle type.")
                cont = True
                return cont
            add_features = input("Do you want to add optional features? (yes/no): ").lower()
            package = Feature_Package()
            if add_features == 'yes':
                print("Available optional features:")
                print("1. Security")
                print("2. Enhanced Safety Features")
                print("3. Entertainment System")
                print("4. Sunroof")
                selected_features = []
                while True:
                    feature_choice = int(input("Enter the number corresponding to the feature you want to add (or type 0 for stop): "))
                    if feature_choice == 0:
                        break
                    elif feature_choice == 1:
                        selected_features.append(Security())
                    elif feature_choice == 2:
                        selected_features.append(EnhancedSafetyFeatures())
                    elif feature_choice == 3:
                        selected_features.append(EntertainmentSystem())
                    elif feature_choice == 4:
                        selected_features.append(Sunroof())
                    else:
                        print("Invalid choice.")
                for feature in selected_features:
                    package.add_optional_feature(feature)
            order = Order(name,order_id,vehicle,package)
            found = self.__dealership.add_vehicle_to_order(order)
            if not found:
                print("The vehicle does not exist")
            else:
                print("Vehicle added succefully to cart")

        elif command == 2:
            orders = self.__dealership.view_order()
            print("Your order is as follows: \n")
            for order in orders:
                print(order)

        elif command == 3:
            vehicles = self.__dealership.view_vehicle()
            print("The following vehicles are available")
            if vehicles == None:
                print("Sorry, No vehicle available at this time")
            for vehicle in vehicles:
                print(vehicle)
        elif command == 4:
            price = float(input("Enter the price: "))
            vehicles = self.__dealership.search_price(price)
            for vehicle in vehicles:
                print(vehicle)
        elif command == 5:
            print(". Available optional features:")
            print("1. Security")
            print("2. Enhanced Safety Features")
            print("3. Entertainment System")
            print("4. Sunroof")
            choice = int(input("Please enter number: "))
            feature = OptionalFeature
            if choice == 1:
                feature = Security()
            elif choice == 2:
                feature = EnhancedSafetyFeatures()
            elif choice == 3:
                feature = EntertainmentSystem()
            elif choice == 4:
                feature = Sunroof()
            else:
                print("Enter valid choice")
            vehicles= self.__dealership.search_by_feature(feature)
            for vehicle in vehicles:
                print(vehicle)

        elif command == 6:
            max,min= self.__dealership.highest_and_lowest_price()
            if max is None and min is None:
                print("No vehicles available")
            print("Vehicle most expensive: ")
            print(f'{max}\n')
            print("vehicle leaest expensive")
            print(str(min))
        
        elif command == 7:
            name = input("The name to remove: ")
            id = input("The order_id to remove: ")
            found = self.__dealership.remove_vehicle_from_order(name,id)
            if found:
                print("Removed Succefully")

        elif command == 8:
            cont = False
        else:
            print("Enter Valid Number from Options")
        return cont
  
def main():
    app = DealershipApp()

    cont = True
    while cont is True:
        app.show_menu()
        command = int(input("Enter your choice: "))
        cont = app.process_command(command)

if __name__ == "__main__":
    main()


    







