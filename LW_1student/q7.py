# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------------+------------+
# |           Input            |   Output   |
# |   rs    cs    rd    cd     |            |
# +----------------------------+------------+
# |    0     0     7     4     |     7       |
# |    3     2    10     9     |     7       |
# |    9     3    17    11     |     8       |
# +----------------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
rs, cs, rd, cd = input().split(" ")
rs = int(rs)
cs = int(cs)
rd = int(rd)
cd = int (cd)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
diagonal = cd - cs
straight = rd - rs - diagonal
print(diagonal + straight)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.