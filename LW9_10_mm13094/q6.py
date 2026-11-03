# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#
def recur_find(count, notes, keyword):
    if count + len(keyword) > len(notes):
        print(-1)
    elif notes[count:count + len(keyword)] == keyword:
        print(count)
    else:
        recur_find(count + 1, notes, keyword)

def my_find(notes, keyword):
    # WRITE YOUR CODE HERE
    recur_find(0, notes, keyword)


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

    my_find('banana', 'na')
    # Should print: 2

    my_find('ban', 'na')
    # Should print: -1

    my_find('banana', 'ban')
    # Should print: 0

    my_find('aaaa', 'aa')
    # Should print: 0

    my_find('', 'a')
    # Should print: -1

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py