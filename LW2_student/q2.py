# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       m        |            |
# +----------------+------------+
# |       8        |    North        |
# |       15       |     West       |
# |      253       |     East       |
# +----------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variable here.
m = int(input())

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
degree = 90 * (m - ((m // 4) * 4))

if degree == 0:
    print("North")
elif degree == 90:
    print("East")
elif degree == 180:
     print("South")
else:
    print("West")


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.