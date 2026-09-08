# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def decode_value(clue_number):
    fifth = clue_number % 10
    fourth = (clue_number % 100) // 10
    third = (clue_number % 1000) // 100
    second = (clue_number % 10000) // 1000
    first = clue_number // 10000
    verification_score = first + second * 2 + third * 3 + fourth * 4 + fifth * 5
    return verification_score



# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
clue_number = int(input("Clue Number: "))



# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

result = decode_value(clue_number)
print(result)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-------------+--------+
# | clue_number | Output |
# +-------------+--------+
# | 58324       | 58     |
# | 91736       | 74     |
# | 42618       | 70     |
# | 73105       | 41     |
# | 99999       | 135    |
# +-------------+--------+