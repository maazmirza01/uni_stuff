# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def potion_doses(hurdle_count, max_jump_height):
    # WRITE YOUR CODE HERE
    highest = 0
    for hurdle_num in range(hurdle_count):
        hurdle = int(input())
        if hurdle > highest:
            highest = hurdle
    count = highest - max_jump_height
        
    return count
        


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

    #print(potion_doses(4, 3))
    # [ Input -> 1]
    # [ Input -> 2]
    # [ Input -> 3]
    # [ Input -> 2]
    # Should print: 0

    print()

    print(potion_doses(5, 7))
    # [ Input -> 2]
    # [ Input -> 7]
    # [ Input -> 8]
    # [ Input -> 10]
    # [ Input -> 3]
    # Should print: 3

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py
