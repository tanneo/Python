#number of cars
cars = 100
#number of seats in each car for passengers
space_in_a_car = 4.0
#number of drivers available today
drivers = 30 
#number of passengers that need a life
passengers = 90
#cars not driven is the number of total cars less the number of drivers available on that day
cars_not_driven = cars - drivers
#cars driven is the same as the number of drivers that are avialable that day 
cars_driven = drivers
#car pool capacity is number of cars
car_pool_capacity = cars_driven * space_in_a_car
#average number of passengers in the car are the number of total cars divided by the number of cars that are available 
average_passenger_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", car_pool_capacity, "people today")
print("We have", passengers, "to take in the cars today")
print("We are putting about", average_passenger_per_car, "in each car today")

# If you change space in car from 4.0 to 4, it effects car_pool_capacity variable in calculation from 12.0 to a full integer of 120
#