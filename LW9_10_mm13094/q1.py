# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#
def primary_diagonal_sum(net_changes):
    sum = 0
    for i in range(len(net_changes)):
        sum += net_changes[i][i]        
    return sum
def secondary_diagonal_sum(net_changes):
    sum = 0
    for i in range(len(net_changes)):
        sum += net_changes[i][len(net_changes) - 1 - i]
        
    return sum

def diagonal_difference(net_changes):
    # WRITE YOUR CODE HERE
    primary_sum = primary_diagonal_sum(net_changes)
    secondary_sum = secondary_diagonal_sum(net_changes)
    if primary_sum > secondary_sum:
        return primary_sum - secondary_sum
    else:
        return secondary_sum - primary_sum


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

    print(diagonal_difference(
        [
            [11, 2, 4], 
            [4, 5, 6], 
            [10, 8, -12]
        ]))
    # Should print: 15

    print(diagonal_difference(
        [
            [1, 2], 
            [3, 10]
        ]))
    # Should print: 6

    print(diagonal_difference(
        [
            [-5]
        ]))
    # Should print: 0

    print(diagonal_difference(
        [
            [2]
        ]))
    # Should print: 0

    print(diagonal_difference(
        [
            [1, 2], 
            [3, 4]
        ]))
    # Should print: 0

    print(diagonal_difference(
        [
            [3, 5, 7], 
            [1, 4, 9], 
            [2, 8, 6]
        ]))
    # Should print: 0

    print(diagonal_difference(
        [
            [10, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]))
    # Should print: 9

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py