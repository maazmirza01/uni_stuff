# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def power_pyramid(row_count):
    # WRITE YOUR CODE HERE
    for i in range(0, row_count):
        for j in range(0, i + 1):
            print(2**j, end=" ")
        for k in range(i-1, -1, -1):
            print(2**k, end=" ")
        print()


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

    power_pyramid(3)
    ''' Should print:
    1
    1 2 1
    1 2 4 2 1
    '''

    power_pyramid(1)
    ''' Should print:
    1
    '''

    power_pyramid(2)
    ''' Should print:
    1
    1 2 1
    '''

    power_pyramid(6)
    ''' Should print:
    1
    1 2 1
    1 2 4 2 1
    1 2 4 8 4 2 1
    1 2 4 8 16 8 4 2 1
    1 2 4 8 16 32 16 8 4 2 1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py