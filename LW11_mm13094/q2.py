def to_binary(number):
    # WRITE YOUR CODE HERE
    if number == 0:
        return "0"
    
    if number == 1:
        return "1"
    else:
        if number >= 0:
            return to_binary(number // 2) + str(number % 2)
        else:
            if number == -1:
                return "-1"
            else:
                number = number * -1
                return "-" + to_binary(number//2) + str(number % 2)



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

    print(to_binary(-3))
    # Should print: -11

    print(to_binary(0))
    # Should print: 0

    print(to_binary(156))
    # Should print: 10011100

    print(to_binary(42))
    # Should print: 101010

    print(to_binary(-40))
    # Should print: -101000

    print(to_binary(-42))
    # Should print: -101010

    print(to_binary(1))
    # Should print: 1

    print(to_binary(8))
    # Should print: 1000

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py
