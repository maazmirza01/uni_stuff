# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def reverse_number(locker_number):
    # WRITE YOUR CODE HERE
    reverse = 0
    while True:
        quotient = locker_number // 10
        remainder = locker_number % 10
        reverse = reverse + remainder
        locker_number = quotient 
        if quotient == 0:
            break
        else: 
            reverse = reverse * 10
    return reverse




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

    print(reverse_number(12345))
    # Should print: 54321

    print(reverse_number (33602))
    # Should print: 20633

    print(reverse_number(1200))
    # Should print: 21

    print(reverse_number(507))
    # Should print: 705

    print(reverse_number(91))
    # Should print: 19

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py