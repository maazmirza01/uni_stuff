# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def number_trail(start_value):
    # WRITE YOUR CODE HERE
    end_value = start_value - 1
    for i in range(start_value, 0, -1):
        
        for j in range(start_value, end_value, -1):
            print(j, end=" ")
        print()

        end_value = end_value - 1


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

    number_trail(5)
    ''' Should print:
    5
    5 4
    5 4 3
    5 4 3 2
    5 4 3 2 1
    '''

    number_trail(1)
    ''' Should print:
    1
    '''

    number_trail(2)
    ''' Should print:
    2
    2 1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py
