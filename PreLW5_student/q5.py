# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def hollow_square(size):
    # WRITE YOUR CODE HERE
    for i in range(size):
        if i == 0 or i == size - 1:
            for j in range(size):
                print("*", end="")
            print()
        else:
            print("*", end="")
            for j in range(size-2):
                print(" ", end="")
            print("*")
    


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

    hollow_square(5)
    ''' Should print:
    *****
    *   *
    *   *
    *   *
    *****
    '''

    hollow_square(1)
    ''' Should print:
    *
    '''

    hollow_square(3)
    ''' Should print:
    ***
    * *
    ***
    '''


    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py
