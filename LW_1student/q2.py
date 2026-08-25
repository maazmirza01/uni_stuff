# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |    T     C     |            |
# +----------------+------------+
# |   10     3     |     3      |
# |  100    10     |     100       |
# |  130     4     |       52     |
# +----------------+------------+
T, C = input("enter T and C respectively! ").split(" ")
T = int(T)
C = int(C)

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
points_per_question = T / 10
score = points_per_question * C
print(C)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.