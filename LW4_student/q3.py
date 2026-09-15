# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def collatz_sequence(starting_number):
    # WRITE YOUR CODE HERE
    current_number = starting_number
    while True:
        if current_number == 1 or current_number == 5 or current_number == 17:
            break
        else:    
            print(current_number, end=", ")
            if current_number % 2 == 0:
                current_number = current_number // 2
            else:
                current_number = 3 * current_number - 1
    print(current_number)


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

    collatz_sequence(1)
    # Should print: 1

    collatz_sequence(3)
    # Should print: 3, 8, 4, 2, 1

    collatz_sequence(8)
    # Should print: 8, 4, 2, 1

    collatz_sequence(14)
    # Should print: 14, 7, 20, 10, 5

    collatz_sequence(17)
    # Should print: 17

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#
    


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py