def sum67(lst):
    # WRITE YOUR CODE HERE
    sum = 0
    stop = False
    for num in lst:
        if stop == False:
            if num == 6:
                stop = True
            else:
                sum += num
        else:
            if num == 7:
                stop = False
    return sum



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
    print(sum67([1, 2, 2]))
    # Should print: 5

    print(sum67([4, 2, 2, 6, 99, 99, 7]))
    # Should print: 8

    print(sum67([9, 1, 6, 7, 0]))
    # Should print: 10

    print(sum67([6, 7]))
    # Should print: 0

    print(sum67([6, 6, 7, 7]))
    # Should print: 7

    print(sum67([1, 1, 6, 4, 5, 8, 0, 7, 2]))
    # Should print: 4

    print(sum67([6, 7, 1, 2, 3, 7]))
    # Should print: 13

    print(sum67([1, 2, 3, 6, 7, 4, 5]))
    # Should print: 15

    print(sum67([]))
    # Should print: 0

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py