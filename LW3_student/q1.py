# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def format_name(name, order_hour):
    if order_hour > 19:
        name = name.upper()
    else:
        name = name.lower()
    print(name)



# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
name = input("Write your name: ")
order_hour = int(input("Order hour: "))



# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.

format_name(name, order_hour)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +--------+------------+--------+
# | name   | order_hour | Output |
# +--------+------------+--------+
# | waQar  | 20         | WAQAR  |
# | FatIMA | 19         | fatima |
# | AHMED  | 22         | AHMED  |
# | kaRIm  | 5          | karim  |
# | uShNa  | 10         | ushna  |
# +--------+------------+--------+