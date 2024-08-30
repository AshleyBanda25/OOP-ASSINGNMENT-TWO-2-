# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Engine is starting."

# Derived class Car
class Car(Vehicle):
    def start_engine(self):
        return "Car engine is roaring!"

# Derived class Truck
class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine is rumbling!"

# Function demonstrating polymorphism
def start_any_vehicle(vehicle):
    print(vehicle.start_engine())

# Example usage
if __name__ == "__main__":
    # Create instances of Car and Truck
    my_car = Car("Toyota", "Camry")
    my_truck = Truck("Ford", "F-150")

    # Demonstrate polymorphism
    start_any_vehicle(my_car)   # Output: Car engine is roaring!
    start_any_vehicle(my_truck) # Output: Truck engine is rumbling!


'''Explanation
Inheritance
Base Class (Vehicle): This is the common ancestor class that holds 
attributes (make and model) and a method (start_engine) that is shared by all vehicles.
Derived Classes (Car and Truck): These classes inherit from the Vehicle class. 
They override the start_engine method to provide specific implementations for cars 
and trucks. This is where the specific behavior for each type of vehicle is defined.

Polymorphism
Function start_any_vehicle: This function takes a vehicle object as a parameter and 
calls its start_engine method. Since vehicle could be an instance of any class that 
inherits from Vehicle, the actual method that gets called depends on the object's
 class. This is known as polymorphism.

How It Works

Inheritance allows the Car and Truck classes to reuse the Vehicle class's a
ttributes and methods. Both derived classes extend the Vehicle class, inheriting 
its properties and methods.
Polymorphism is demonstrated by the start_any_vehicle function, which can accept 
any Vehicle type object (including Car and Truck). It calls the start_engine method 
on the object, and the appropriate method implementation for that specific vehicle type is executed.

This approach allows for flexible and extendable code where new vehicle types
 can be added easily with their own specific behaviors while still using a common 
 interface defined in the Vehicle class.
'''