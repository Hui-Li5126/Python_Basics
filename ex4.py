
# = assigns the value on the right to a variable on the left
# == tests whether two things have the same value.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_drive = drivers
carpool_capacity = cars_drive * space_in_a_car
average_passengers_per_car = passengers / cars_drive

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")
