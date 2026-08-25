# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |    N     K     |            |
# +----------------+------------+
# |   50     0     |     50       |
# |  100    50     |       50     |
# |   25    12     |       13     |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
N, K = input("enter N and K respectively! ").split(" ")
N = int(N)
K = int(K)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
bilal_score = N - K
print("here is bilal's score = ", bilal_score) 

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.