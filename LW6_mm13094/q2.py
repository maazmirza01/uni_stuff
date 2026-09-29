# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def rotate_message(display_message, rotation_count):
    # WRITE YOUR CODE HERE
    rotation_count = rotation_count % len(display_message)
    message = display_message[rotation_count:] + display_message[:rotation_count]
    return message



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

    print(rotate_message('campus', 3))
    # Should print: puscam
     
    print(rotate_message('campus', -2))
    # Should print: uscamp
     
    print(rotate_message('campus', 8))
    # Should print: mpusca
     
    print(rotate_message('campus', -8))
    # Should print: uscamp

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q2.py