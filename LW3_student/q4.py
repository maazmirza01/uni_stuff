# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def phone_rating(speed_score, lag_time, battery_mah):
    if speed_score > 50 and lag_time < 0.7 and battery_mah > 4500:
        return "10"
    elif speed_score > 50 and lag_time < 0.7:
        return "9"
    elif lag_time < 0.7 and battery_mah > 4500:
        return "8"
    elif speed_score > 50 and battery_mah > 4500:
        return "7"
    elif speed_score > 50 or lag_time < 0.7 or battery_mah > 4500:
        return "6"
    else:
        return "5"



# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.

speed_score = int(input("Speed Score: "))
lag_time = float(input("Lag Time: "))
battery_mah = int(input("Battery mAh: "))

# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

result = phone_rating(speed_score, lag_time, battery_mah)
print(result)
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# The first two testcases are from the Sample section.
#
# +-------------+----------+-------------+--------+
# | speed_score | lag_time | battery_mah | Output |
# +-------------+----------+-------------+--------+
# | 60          | 0.5      | 5000        | 10     |
# | 50          | 0.7      | 4500        | 5      |
# | 60          | 0.5      | 4000        | 9      |
# | 45          | 0.5      | 5000        | 8      |
# | 60          | 0.9      | 5000        | 7      |
# | 60          | 0.9      | 4000        | 6      |
# | 45          | 0.5      | 4000        | 6      |
# | 45          | 0.9      | 5000        | 6      |
# +-------------+----------+-------------+--------+