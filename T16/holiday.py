"""
Practical Task 1
Follow these steps:

● Create a Python file called holiday.py.

"""

# The 3 (input)s will ask user for the flight, hotel and car details
# The details are stored as (variables) - this is an (argument)
# Function can be re-use and an argument can be pass through 
# The (hotel_cost) and (car_rental) functions calculate the amount of nights/days
# (plane_cost) will fix the city name for clarity and give the cost accordingly
# (holiday_cost) will sum up everything and composes string sentences
# Fianlly, the program will print the message of the total for the holiday

city_flight = str(input("We fly to: Paris, New York, Tokyo and London. What's your destination? ")).upper()
num_nights = int(input("For how many nights? "))
rental_days = int(input("How many days you will be hiring a car for? "))

def hotel_cost(nights_input):

    cost_per_night = 65
    total = cost_per_night * nights_input 

    # print(total)

    return total

def plane_cost(destination_input):

    city = ""
    cost = 0

    if "PARIS" in destination_input or destination_input == "PARIS":
        city += "Paris"
        cost += 156
    elif "NEW" in destination_input or "YORK" in destination_input or destination_input == "NEW YORK":
        city += "New York"
        cost += 1578
    elif "TOK" in destination_input or destination_input == "TOKYO":
        city += "Tokyo"
        cost += 2078
    elif "LOND" in destination_input or destination_input == "LONDON":
        city += "London"
        cost += 88
    else:
        print("\nI'm sorry but we do not fly there! Please try again...")

    cost_and_city = [("city", city), ("cost", cost)]
    cost_and_city = dict(cost_and_city)

    return cost_and_city

def car_rental(days_input):

    cost_per_day = 50
    total = cost_per_day * days_input

    return total

def holiday_cost(hotel,flight,car):

    holiday_total = hotel + flight["cost"] + car

    plane_des = f"\nThe flight ticket for flying to {flight["city"]} will be £{flight["cost"]}."
    hotel_des = f"\nStaying in the hotel for {num_nights} night(s). This will be £{hotel} in total."
    car_des = f"\nRenting a car for {rental_days} day(s). This will be £{car} in total."

    description = f"{plane_des}{hotel_des}{car_des}\n\nThe grand total for your holiday is £{holiday_total}.\n"

    return description

from_hotel = hotel_cost(num_nights)
from_flight = plane_cost(city_flight)
from_car = car_rental(rental_days)

holiday_result = holiday_cost(from_hotel, from_flight, from_car)

print(holiday_result)