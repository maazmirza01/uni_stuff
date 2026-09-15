# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
# Write the required function(s) below.

def best_choice(board_count, weight_limit):
    # WRITE YOUR CODE HERE
    pass


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

    # Note: Inputs to be entered are labelled as [ Input -> X ] where X is the input.

    best_choice(3, 6)
    # [ Input -> 3]
    # [ Input -> 4]
    # [ Input -> 4]
    # [ Input -> 5]
    # [ Input -> 5]
    # [ Input -> 7]
    # [ Input -> 5]
    # [ Input -> 2]
    # [ Input -> 5]
    # Should print: 12

    print()

    best_choice(2, 6)
    # [ Input -> 3]
    # [ Input -> 6]
    # [ Input -> 8]
    # [ Input -> 5]
    # [ Input -> 4]
    # [ Input -> 9]
    # Should print: No Board

    print()

    best_choice(2, 8)
    # [ Input -> 3]
    # [ Input -> 8]
    # [ Input -> 8]
    # [ Input -> 5]
    # [ Input -> 5]
    # [ Input -> 6]
    # Should print: 25

    print()

    best_choice(3, 15)
    # [ Input -> 2]
    # [ Input -> 6]
    # [ Input -> 16]
    # [ Input -> 3]
    # [ Input -> 6]
    # [ Input -> 19]
    # [ Input -> 5]
    # [ Input -> 4]
    # [ Input -> 33]
    # Should print: No Board

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#

    

# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q6.py