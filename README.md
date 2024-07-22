
# Dealership Management System

## Overview

The Dealership Management System is a Python-based application designed to manage the inventory of vehicles, process orders, and handle various functionalities for a vehicle dealership. It allows users to add vehicles to the inventory, create orders with optional features, view available vehicles and orders, search for vehicles by price and features, and manage vehicle orders.

## Features

- **Inventory Management**: Add, view, and remove vehicles from the dealership inventory.
- **Order Management**: Create, view, and remove vehicle orders with optional feature packages.
- **Vehicle Search**: Search for vehicles by price and specific features.
- **Price Analysis**: Identify the most and least expensive vehicles in the inventory.

## Classes and Modules

### Dealership

- **Attributes**:
  - `name`: The name of the dealership.
  - `address`: The address of the dealership.
  - `inventory`: A list of vehicles available in the dealership.
  - `orders`: A list of orders placed in the dealership.

- **Methods**:
  - `add_vehicle(vehicle)`: Adds a vehicle to the inventory.
  - `add_vehicle_to_order(order)`: Adds a vehicle to an order if it matches the criteria.
  - `search_by_feature(feature)`: Searches for vehicles by a specific feature.
  - `remove_vehicle_from_inventory(vehicle)`: Removes a vehicle from the inventory and associated orders.
  - `remove_vehicle_from_order(name, order_id)`: Removes a vehicle from a specific order.
  - `view_order()`: Returns the list of orders.
  - `view_vehicle()`: Returns the list of vehicles.
  - `highest_and_lowest_price()`: Returns the most and least expensive vehicles.
  - `search_price(price)`: Searches for vehicles by a specific price.
  - `get_vehicle_from_vehicledb()`: Retrieves vehicles from the database.
  - `get_orders_from_orderdb()`: Retrieves orders from the database.
  - `save_order_to_vehicledb()`: Saves the current vehicle inventory to the database.
  - `save_order_to_orderdb()`: Saves the current orders to the database.

### Vehicle and Subclasses

- **Vehicle**: Base class for all vehicle types.
- **Sedan, Truck, SUV, Minivan**: Subclasses of `Vehicle` with specific attributes and base prices.

### Order

- **Attributes**:
  - `customer_name`: The name of the customer.
  - `order_id`: The unique ID for the order.
  - `vehicle`: The vehicle associated with the order.
  - `feature_package`: The package of optional features included in the order.

- **Methods**:
  - `final_price()`: Calculates the final price of the order.
  - `convert_to_list()`: Converts the order details to a list format for saving to the database.

### OptionalFeature and Subclasses

- **OptionalFeature**: Base class for all optional features.
- **EnhancedSafetyFeatures, Security, EntertainmentSystem, Sunroof**: Subclasses of `OptionalFeature`.

### Repositories

- **OrderRepository**: Handles reading from and writing to the orders database.
- **VehicleRepository**: Handles reading from and writing to the vehicle inventory database.

### DealershipApp

- **Attributes**:
  - `dealership`: An instance of `Dealership`.

- **Methods**:
  - `show_menu()`: Displays the menu of options.
  - `process_command(command)`: Processes the user command from the menu.

## How to Run

1. Ensure Python is installed on your machine.
2. Clone the repository.
3. Install required dependencies (if any).
4. Run the `DealershipApp` by executing the `main()` function in `DealershipApp.py`.

```bash
python dealership_app.py
```

## Example Usage

1. **Add Vehicle to Inventory**:
    ```python
    dealership.add_vehicle(Sedan("Toyota Camry", "Blue", 2023, 5))
    ```

2. **Create an Order**:
    ```python
    order = Order("John Doe", "123456", sedan1, package1)
    dealership.add_vehicle_to_order(order)
    ```

3. **View Orders**:
    ```python
    orders = dealership.view_order()
    for order in orders:
        print(order)
    ```

4. **Search Vehicles by Price**:
    ```python
    vehicles = dealership.search_price(30000)
    for vehicle in vehicles:
        print(vehicle)
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
