''' Program to calculate total holiday cost to a selected city for entered 
days of acoomodation and car rental'''

print("\n\t\t Total holiday cost")
print("\t\t-------------------")

# Function to calculate the hotel cost based on the number days of stay
def hotel_cost(num_nights):
    hotel_cost_dict = {"Edinburgh" : 250, "Belfast" : 200, "Glassgow" : 300, "Bristol" : 100}
    hotel_stay_cost = (hotel_cost_dict[city_flight_options[int(city_flights_choice)]]) * int(num_nights)
    return hotel_stay_cost



# Function to calculate the plane cost based on the selected city    
def plane_cost(city_flight):
    plane_cost_dict = {"Edinburgh" : 700, "Belfast" : 500, "Glassgow" : 1000, "Bristol" : 400}
    plane_travel_cost = plane_cost_dict[city_flight_options[int(city_flights_choice)]]
    return plane_travel_cost

# Function to calculate the car rental cost based on the number days of hire
def car_rental(rental_days):
    car_rental_dict = {"Edinburgh" : 150, "Belfast" : 200, "Glassgow" : 250, "Bristol" : 100}     
    car_hire_rent = car_rental_dict[city_flight_options[int(city_flights_choice)]] * int(rental_days)
    return car_hire_rent    
 
# Function to call hotel_cost, plane_cost and rental_cost functions and calculates the total holiday cost 
def holiday_cost(stay_cost, flight_cost, car_rental_days):
    acc_cost = hotel_cost(stay_cost)
    travel_cost = plane_cost(flight_cost)
    car_hire = car_rental(car_rental_days)
    total_cost = acc_cost + travel_cost + car_hire
    return total_cost

city_flight_options = {1: "Edinburgh", 2 : "Belfast", 3 : "Glassgow", 4 : "Bristol"}

# Asks the users to enter the input and checks if entered input is valid
city_flights_choice = input("\n Enter the city you want to travel. Enter 1 for Edinburgh , 2 for Belfast, 3 for Glassgow, 4 for Bristol : ")
while not city_flights_choice.isnumeric() or int(city_flights_choice) <= 0  or int(city_flights_choice) > 4:
    print("\n !!! Enter a valid option between 1 and 4!!!")
    city_flights_choice = input("\nEnter the city you want to travel. Enter 1 for Edinburgh , 2 for Belfast, 3 for Glassgow, 4 for Bristol : ")
    
num_nights = input("\n Enter the number of days you would like to stay: ")
while not num_nights.isnumeric() or int(num_nights) <= 0:
    print("\n !!! Enter a valid number of nights!!!")
    num_nights = input("\nEnter the number of days you would like to stay: ")

car_rental_days = input("\n Enter the number of days you need to rent the car for : ")
while not car_rental_days.isnumeric() or int(car_rental_days) <= 0 or int(car_rental_days) > int(num_nights):
    print("\n !!! Enter a valid number of days less than or equal to number of days of stay!!!")
    car_rental_days = input("\nEnter the number of days you need to rent the car for : ")


holiday_total_cost = holiday_cost(int(num_nights), city_flight_options[int(city_flights_choice)], int(car_rental_days))
print(f"\nTotal holiday cost to {city_flight_options[int(city_flights_choice)]} for {num_nights} days accomodation and {car_rental_days} days car rental is {holiday_total_cost} \n")

    




