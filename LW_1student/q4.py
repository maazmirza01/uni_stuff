# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------+------------+
# |        Input         |   Output   |
# |    L      W      C   |            |
# +----------------------+------------+
# |   11     15     50   |    2600        |
# | 1000   1000   1000   |   4000 000         |
# |   67     37     23   |    4784        |
# +----------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
L, W, C = input().split(" ")
L = int(L)
W = int(W)
C = int(C)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
perimeter = 2 * (L + W)
cost = perimeter * C
print(cost)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.