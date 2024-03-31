class Vehicle:
    def __init__(self, model:str, base_price:float, color:str, model_year:int):
        self.__model = model
        self.__base_price = base_price
        self.__color = color
        self.__model_year = model_year
    
    @property
    def model(self):
        return self.__model

    @property
    def base_price(self):
        return self.__base_price

    @property
    def color(self):
        return self.__color

    @property
    def model_year(self):
        return self.__model_year

    @property
    def base_price(self):
        return self.__base_price
    
    # def convert_to_list(self,name:str) -> list[str]:
    #     lst = []
    #     lst.append(name)
    #     lst.append(self.__model)
    #     lst.append(self.__base_price)
    #     lst.append(self.__color)
    #     lst.append(self.__model_year)
    #     return lst
    
    def __str__(self) -> str:
        return f'Model:{self.__model}\nBase_Price:{self.__base_price}\nColor:{self.__color}\nModel_Year:{self.__model_year}'
    
    def __repr__(self) -> str:
        return str(self)

class Sedan(Vehicle):
    def __init__(self, model:str, color:str, model_year:int,num_seats:int):
        super().__init__(model, 30000, color, model_year)
        self.__num_seats = num_seats

    @property
    def num_seats(self):
        return self.__num_seats
    
    def __str__(self) -> str:
        return f'{super().__str__()}\nNumber of Seats: {self.__num_seats}\n'
    def __repr__(self):
        return str(self)

class Truck(Vehicle):
    def __init__(self, model:str, color:str, model_year:int, cargo_bed_size:str):
        super().__init__(model, 35000, color, model_year)
        self.__cargo_bed_size = cargo_bed_size

    @property
    def cargo_bed_size(self):
        return self.__cargo_bed_size

    def __str__(self) -> str:
        return f'{super().__str__()}\nCargoBedSize: {self.__cargo_bed_size}\n'
    def __repr__(self):

        return str(self)

    
class SUV(Vehicle):
    def __init__(self, model:str, color:str, model_year:int, roof_rack_type:str):
        super().__init__(model, 40000, color, model_year)
        self.__roof_rack_type = roof_rack_type
    
    @property
    def roof_rack_type(self):
        return self.__roof_rack_type

    def __str__(self) -> str:
        return f'{super().__str__()}\nRoofrack Type: {self.__roof_rack_type}\n'
    def __repr__(self):
        return str(self)
    
class Minivan(Vehicle):
    def __init__(self, model:str, color:str, model_year:int, sliding_doors: bool, towing_capacity: int):
        super().__init__(model, 45000, color, model_year)
        self.__sliding_doors = sliding_doors
        self.__towing_capacity = towing_capacity

    @property
    def sliding_doors(self):
        return self.__sliding_doors

    @property
    def towing_capacity(self):
        return self.__towing_capacity
    
    def __str__(self) -> str:
        return f'{super().__str__()}\nSlidingDoors: {self.__sliding_doors}\nTowing Capacity: {self.__towing_capacity}'
    def __repr__(self):
        return str(self)

class OptionalFeature:
    def __init__(self, name:str, price:float):
        self.__name = name
        self.__price = price
    
    @property
    def name(self):
        return self.__name 
    @property
    def price(self):
        return self.__price
    
    def __str__(self) -> str:
        return f'Feature_Name:{self.__name}\nFeature_Price:{self.__price}'
    
    def __repr__(self) -> str:
        return str(self)
    

class EnhancedSafetyFeatures(OptionalFeature):
    def __init__(self):
        super().__init__("Enhanced Safety Features", 3000)

class Security(OptionalFeature):
    def __init__(self):
        super().__init__("Security", 1000)

class EntertainmentSystem(OptionalFeature):
    def __init__(self):
        super().__init__("Entertainment System", 2000)

class Sunroof(OptionalFeature):
    def __init__(self):
        super().__init__("Sunroof", 2500)


# class CustomizedVehicle(Vehicle):
#     def __init__(self, base_vehicle:Vehicle):
#         super().__init__(base_vehicle.model, base_vehicle.base_price, base_vehicle.color, base_vehicle.model_year)
#         self.__base_vehicle = base_vehicle
#         self.__optional_features:list[OptionalFeature]=[]

#     def add_optional_feature(self, feature:OptionalFeature):
#         if isinstance(feature, (EnhancedSafetyFeatures, Security, EntertainmentSystem, Sunroof)):
#             self.__optional_features.append(feature)
#         else:
#             print("Error: This optional feature is not allowed for customization.")

    
#     def __iter__(self):
#         self.__index = -1
#         return self
    
#     def __next__(self):
#         if self.__index >= len(self.__optional_features)-1:
#             raise StopIteration
#         self.index += 1
#         return self.__optional_features[self.__index]

#     def get_final_price(self):
#         total_price = super().get_final_price()
#         for feature in self.__optional_features:
#             total_price += feature.price
#         return total_price
    
#     def __str__(self) -> str:
#         output =''
#         for feature in self.__optional_features:
#             output += str(feature) + '\n'
#         return f'{self.__base_vehicle}\nOptional Features :{output}'
    
#     def __repr__(self) -> str:
#         return str(self)


class Feature_Package:
    def __init__(self) -> None:
        self.__optional_feature:list[OptionalFeature] = []

    def __iter__(self):
        self.index = -1
        return self
    
    def __next__(self):
        if self.index >= len(self.__optional_feature)-1:
            raise StopIteration
        self.index += 1
        return self.__optional_feature[self.index]

    def add_optional_feature(self, feature:OptionalFeature):
        if isinstance(feature, (EnhancedSafetyFeatures, Security, EntertainmentSystem, Sunroof)):
            self.__optional_feature.append(OptionalFeature(feature.name, feature.price))
        else:
            print("Error: This optional feature is not allowed for customization.")
    
    def get_total_featureprice(self):
        total_price = 0.0
        for feature in self.__optional_feature:
            total_price += feature.price
        return total_price
    
    def __str__(self) -> str:
        output = ''
        for feature in self.__optional_feature:
            output += str(feature) +'\n'
        return f'{output}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(object,Feature_Package):
            for option in self.__optional_feature:
                x = option.name == option.price
            return x
        else:
            return False
        


def main():
    vehicles = [
        Sedan("Toyota Camry", "Blue", 2023, 5),
        Truck("Ford F150", "Black", 2022, "Short Bed"),
        SUV("Honda CR-V", "Red", 2023, "Crossbar"),
        Minivan("Chrysler Pacifica", "White", 2024, True, 3500)
    ]
    
    for vehicle in vehicles:
        print(vehicle)

if __name__ == "__main__":
    main()
