# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
# Write the required function(s) below.

def sum_digits(n):
    # WRITE YOUR CODE HERE
    total = 0
    while True:
        total = total + n % 10
        n = n // 10
        if n == 0:
            if total < 10:
                break
            else:
                n = total
                total = 0
    return total


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    print(sum_digits(24))
    # Should print: 6

    print(sum_digits(0))
    # Should print: 0

    print(sum_digits(1092))
    # Should print: 3

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py
