# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def are_you_green(distance_km, refill_cost, fuel_price, target_rate):
    fuel_used_liters = refill_cost / fuel_price
    fuel_consumption_rate = 100 * fuel_used_liters / distance_km
    if target_rate == fuel_consumption_rate:
        print("Just met the target.")
    elif target_rate < fuel_consumption_rate:
        difference = fuel_consumption_rate - target_rate
        difference = round(difference, 2)
        print(f"Missed the target by {difference} L/100 km.")
    else:
        difference = target_rate - fuel_consumption_rate
        difference = round(difference, 2)
        print(f"Performed better than the target by {difference} L/100 km.")


# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
distance_km = float(input("Distance KM: "))
refill_cost = float(input("Refill Cost: "))
fuel_price = float(input("Fuel Price: "))
target_rate = float(input("Target rate: "))


# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.
are_you_green(distance_km, refill_cost, fuel_price, target_rate)


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-------------+-------------+------------+-------------+---------------------------------------------------+
# | distance_km | refill_cost | fuel_price | target_rate | Output                                            |
# +-------------+-------------+------------+-------------+---------------------------------------------------+
# | 50.0        | 500.0       | 100.00     | 8.00        | Missed the target by 2.0 L/100 km.                |
# | 50.0        | 500.0       | 100.00     | 10.00       | Just met the target.                              |
# | 50.0        | 500.0       | 100.00     | 14.00       | Performed better than the target by 4.0 L/100 km. |
# | 75.7        | 1200.0      | 90.84      | 12.50       | Missed the target by 4.95 L/100 km.               |
# | 135.7       | 1200.0      | 90.84      | 12.50       | Performed better than the target by 2.77 L/100 km.|
# | 85.7        | 1200.0      | 90.84      | 12.50       | Missed the target by 2.91 L/100 km.               |
# | 95.7        | 1200.0      | 90.84      | 12.50       | Missed the target by 1.3 L/100 km.                |
# | 120.0       | 1200.0      | 100.00     | 10.00       | Just met the target.                              |
# | 115.7       | 1200.0      | 90.84      | 12.50       | Performed better than the target by 1.08 L/100 km.|
# | 125.7       | 1200.0      | 90.84      | 12.50       | Performed better than the target by 1.99 L/100 km.|
# +-------------+-------------+------------+-------------+---------------------------------------------------+