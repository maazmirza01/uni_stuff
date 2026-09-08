# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def fan_speed(current_setting, button_presses):
    remainder = (current_setting + button_presses) % 4
    if remainder == 0:
        result = "OFF"
    elif remainder == 1:
        result = "LOW"
    elif remainder == 2:
        result = "MEDIUM"
    elif remainder == 3:
        result = "HIGH"
    return result



# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
current_setting = int(input("Current Setting: "))
button_presses = int(input("Button Presses: "))



# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

result = fan_speed(current_setting, button_presses)
print(result)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-----------------+----------------+--------+
# | current_setting | button_presses | Output |
# +-----------------+----------------+--------+
# | 3               | 1              | OFF    |
# | 0               | 11             | HIGH   |
# | 0               | 10             | MEDIUM |
# | 3               | 8348           | HIGH   |
# | 2               | 5903787        | LOW    |
# +-----------------+----------------+--------+