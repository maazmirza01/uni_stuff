# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition(s) below.
def fahrenheit_to_celsius(fahrenheit_temp):
    C = (fahrenheit_temp - 32) * (5/9)
    C = round(C, 2)
    return C

def celsius_to_fahrenheit(celsius_temp):
    F = (celsius_temp * (9/5)) + 32
    F = round(F, 2)
    return F


def temp_converter(temperature, target_scale):
    if target_scale == "F":
        F = celsius_to_fahrenheit(temperature)
        print(f"{F} degrees Fahrenheit is the temperature for Sana.")
    
    elif target_scale == "C":
        C = fahrenheit_to_celsius(temperature)
        print(f"{C} degrees celsius is the temperature for Fatima.")



# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
temperature = int(input("Temperature: "))
target_scale = input("target Scale: ")


# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.

temp_converter(temperature, target_scale)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-------------+--------------+------------------------------------------------------+
# | temperature | target_scale | Output                                               |
# +-------------+--------------+------------------------------------------------------+
# | 95          | C            | 35.0 degrees Celsius is the temperature for Fatima.  |
# | 30          | F            | 86.0 degrees Fahrenheit is the temperature for Sana. |
# | 68          | C            | 20.0 degrees Celsius is the temperature for Fatima. |
# | 22          | F            | 71.6 degrees Fahrenheit is the temperature for Sana.|
# | 86          | C            | 30.0 degrees Celsius is the temperature for Fatima. |
# +-------------+--------------+------------------------------------------------------+