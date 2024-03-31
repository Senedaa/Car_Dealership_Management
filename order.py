from vehicle import *

class Order:
    def __init__(self, customer_name:str, order_id:str, vehicle:Vehicle, feature_package:Feature_Package):
        self.__customer_name = customer_name
        self.__order_id = order_id
        self.__vehicle = vehicle
        self.__feature_package = feature_package
    
    @property
    def customer_name(self):
        return self.__customer_name
    @property
    def order_id(self):
        return self.__order_id
    
    @property
    def vehicle(self):
        return self.__vehicle
    
    @property
    def feature_package(self):
        return self.__feature_package
    
    def __str__(self) -> str:
        return f"CustomerName: {self.__customer_name}\nOrder_Id:{self.__order_id}\nVehicle: {self.__vehicle}\nFeature_Package:{self.__feature_package}\nFinal_Price:{self.final_price()}"
    
    def __repr__(self):
        return str(self)
    
    def final_price(self):
        total_price = self.__vehicle.base_price + self.__feature_package.get_total_featureprice()
        return total_price
    
    def convert_to_list(self):
        order = []
        order.append(self.__customer_name)
        order.append(self.__order_id)
        
        if isinstance(self.__vehicle, Sedan):
            order += ["Sedan", self.__vehicle.model, self.__vehicle.base_price, self.__vehicle.color, self.__vehicle.model_year, self.__vehicle.num_seats]
        elif isinstance(self.__vehicle, Truck):
            order += ["Truck", self.__vehicle.model, self.__vehicle.base_price, self.__vehicle.color, self.__vehicle.model_year, self.__vehicle.cargo_bed_size]
        elif isinstance(self.__vehicle, SUV):
            order += ["SUV", self.__vehicle.model, self.__vehicle.base_price, self.__vehicle.color, self.__vehicle.model_year, self.__vehicle.roof_rack_type]
        elif isinstance(self.__vehicle, Minivan):
            order += ["Minivan", self.__vehicle.model, self.__vehicle.base_price, self.__vehicle.color, self.__vehicle.model_year, self.__vehicle.sliding_doors, self.__vehicle.towing_capacity]
        
        for feature in self.__feature_package:
            order += [feature.name, feature.price]
        order.append(self.final_price())
        return order
    def __eq__(self, other: object) -> bool:
        if isinstance(other,Order):
            return self.customer_name == other.customer_name and self.order_id == other.order_id
        else:
            return False


        

def main():


    sedan1 = Sedan("Toyota Camry", "Blue", 2023, 5)
    suv1= SUV("ford", "white", 2023,'standard')

    feature3= Security()
    feature4= EnhancedSafetyFeatures()
    feature5 = EntertainmentSystem()
    package2 = Feature_Package()
    package2.add_optional_feature(feature3)
    package2.add_optional_feature(feature4)
    package2.add_optional_feature(feature5)
    order2 = Order("Amrita Tappa", "2015", suv1, package2)
    print(order2)


    # feature1 = EnhancedSafetyFeatures()
    # feature2 = Security()
    # package1 = Feature_Package()
    # package1.add_optional_feature(feature1)
    # package1.add_optional_feature(feature2)
    # order = Order("John Doe", "123456", sedan1, package1)
    # print(order)
    # print("Final Price:", order.final_price())

if __name__ == "__main__":
    main()
