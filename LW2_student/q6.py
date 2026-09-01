# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +-----------------------+------------+
# |         Input         |   Output   |
# |  w1    w2    w3    s  |            |
# +-----------------------+------------+
# |  2     1     3     6  |     1       |
# |  8     5     4    10  |     2       |
# |  6     5     6    10  |    3        |
# +-----------------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
w1, w2 , w3, s = input().split(" ")
w1 = int(w1)
w2 = int(w2)
w3 = int(w3)
s = int(s)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
trips = 0
if w1 + w2 > s:
    trips += 1 
    if w2 + w3 > s:
        trips = 3
    else:
        trips += 1
elif w1 + w2 + w3 > s:
    trips = 2
else:
    trips += 1

print(trips) 

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.