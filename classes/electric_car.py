"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def increment_battery(self, kwh):
        self.battery_size += kwh
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 80:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")
            
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year, top_speed):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        self.top_speed = top_speed        
        
    def max_speed(self):
        print(f"My {descriptive_name} has a top speed of {self.top_speed} miles/hour!")
        
# my_tesla = ElectricCar(make='tesla',
#                        model='model s',
#                        year = 2019, 
#                        top_speed=135,
#                        battery=80)

# descriptive_name = my_tesla.get_descriptive_name()
# print(descriptive_name)

# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.increment_battery(20)
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.max_speed()