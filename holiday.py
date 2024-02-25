# Function to calculate the cost of hotel stay
def hotel_cost(num_nights):
    # Calculate total cost based on number of nights and fixed cost per night
    total = num_nights * 129 
    return total

# Function to calculate the cost of plane ticket to a given city
def plane_cost(city_flight):
    # Check if the city_flight is valid and exists in the city_costs dictionary
    city_flight = city_flight 
    if city_flight in city_costs:
        # Return the cost of the plane ticket for the specified city
        return city_costs[city_flight]
    else:
        # If the city is not valid, print an error message
        print("Invalid city selection.")
        return None

# Function to calculate the cost of car rental
def car_rental(rental_days):
    total_cost = rental_days * 50
    return total_cost

# Function to calculate the total holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)
    total_cost = hotel + plane + car
    return hotel, plane, car, total_cost

city_options = ["Paris", "Tokyo", "Milan", "Lagos", "Bali"]

# Dictionary containing the costs of plane tickets for each city
city_costs = {
    "Paris": 500,
    "Tokyo": 1000,
    "Milan": 400,
    "Lagos": 700,
    "Bali": 1150
}
# Prompt the user to select a city to fly to from defined list
while True:
    print("What city will you be flying to? Select from the following:")
    for city in city_options:
        print(city)
    
    # Receive user input for the city_flight
    city_flight = input().capitalize()

    # Check if the input city is valid
    if city_flight in city_costs:
        break  # Exit the loop if the city is valid
    else:
        print("Invalid city selection. Please try again.")

# Prompt user input for remaining holiday details
num_nights = int(input("How many nights will you be staying?: "))

rental_days = int(input("How many days will you be renting a car?: "))

# Calculate holiday details and costs
hotel, plane, car, total_cost = holiday_cost(num_nights, city_flight, rental_days)


# Display holiday details and costs to the user
print("\nYour Holiday Details:")
print(f"City: {city_flight.capitalize()}")
print(f"Hotel Cost: £{hotel}")
print(f"Plane Cost: £{plane}")
print(f"Car Rental Cost: £{car}")
print(f"Total Cost: £{total_cost}")