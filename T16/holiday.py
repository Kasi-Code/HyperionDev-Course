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

def plane_cost(destination_input):
    city = ""
    cost = 0

    # New version

    if destination_input == 1:
        city += "Paris"
        cost += 156
    elif destination_input == 2:
        city += "New York"
        cost += 1578
    elif destination_input == 3:
        city += "Tokyo"
        cost += 2078
    elif destination_input == 4:
        city += "London"
        cost += 88
    else:
        print("\nI'm sorry but we do not fly there! Please try again...")
        return None
        
    cost_and_city = {city:cost}
    return cost_and_city

    # Older version

    # if "PARIS" in destination_input or destination_input == "PARIS":
    #     city += "Paris"
    #     cost += 156
    # elif "NEW" in destination_input or "YORK" in destination_input or destination_input == "NEW YORK":
    #     city += "New York"
    #     cost += 1578
    # elif "TOK" in destination_input or destination_input == "TOKYO":
    #     city += "Tokyo"
    #     cost += 2078
    # elif "LOND" in destination_input or destination_input == "LONDON":
    #     city += "London"
    #     cost += 88
    # else:
    #     print("\nI'm sorry but we do not fly there! Please try again...")

    # cost_and_city = [("city", city), ("cost", cost)]
    # cost_and_city = dict(cost_and_city)

    # return cost_and_city

def hotel_cost(nights_input):
    cost_per_night = 65
    total = cost_per_night * nights_input 

    return total

def car_rental(days_input):
    cost_per_day = 50
    total = cost_per_day * days_input

    return total

def holiday_cost(hotel,flight,car):
    if flight is not None:
        flight_city, flight_cost = list(flight.items())[0]

    holiday_total = hotel + flight_cost + car # <-- previously flight["cost"]

    plane_str = f"\nThe flight ticket for flying to {flight_city} will be £{flight_cost}."  # <-- previously flight["city"]
    hotel_str = f"\nStaying in the hotel for {num_nights} night(s) will be £{hotel}."
    car_str = f"\nRenting a car for {rental_days} day(s) will be £{car}."

    description = f"{plane_str}{hotel_str}{car_str}\n\nThe grand total for your holiday is £{holiday_total}.\n"

    return description

# city_flight = str(input("We fly to: Paris, New York, Tokyo and London. What's your destination? ")).upper() # <-- OLD Version

city_flight = int(input("""
    Where would you like to fly to? \n
    1. Paris \t 2. New York
    3. Tokyo \t 4. London \n
    Type the number: """))

num_nights = int(input("\nFor how many nights? "))
rental_days = int(input("How many days you will be hiring a car for? "))

from_hotel = hotel_cost(num_nights)
from_flight = plane_cost(city_flight)
from_car = car_rental(rental_days)

holiday_result = holiday_cost(from_hotel, from_flight, from_car)

print(holiday_result)