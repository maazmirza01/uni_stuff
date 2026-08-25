# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------------+------------+
# |           Input            |   Output   |
# |   b     f      B      F    |            |
# +----------------------------+------------+
# |  100   450   1000   1350   |     13.0       |
# |  200   500   1200   1500   |      9      |
# |  150   500   1050   1500   |     10       |
# +----------------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

b, f, B, F = input().split(" ")
b = int(b)
f = int(f)
B = int(B)
F = int(F)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
num_fruit = F / f
num_base = B / b

print(int(num_fruit + num_base))
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.