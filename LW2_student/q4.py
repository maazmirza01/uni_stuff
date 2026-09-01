# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +------------------+------------+
# |      Input       |   Output   |
# |  A     B     C   |            |
# +------------------+------------+
# |  18   271   31   |    302        |
# |  127  2933  182  |     3115       |
# |  21    2    18   |     39       |
# +------------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

if A >= B >= C:
    print(A + B)
elif A >= C >= B:
    print(A + C)
elif B >= A >= C:
    print(B + A)
elif B >= C >= A:
    print(B + C)
elif C >= A >= B:
    print(A + C)
else:
    print(C + B)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.