# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
# Write the required function(s) below.

def clean_message(draft_message):
    # WRITE YOUR CODE HERE
    count = 0 
    while count < len(draft_message):
        if count == 0 and draft_message[count] == "#":
            draft_message = draft_message[1:]
            count = 0
        elif draft_message[count] == "#":
            draft_message = draft_message[:count - 1] + draft_message[count + 1:]
            count = 0
        else:
            count += 1
    cleaned_message = draft_message
    return cleaned_message
        



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

    print(clean_message('hello#!'))
    # Should print: hell!

    print(clean_message('abc##d'))
    # Should print: ad

    print(clean_message('##abc'))
    # Should print: abc

    print(clean_message('a##bc'))
    # Should print: bc

    print(clean_message('abc###'))
    # Should print:

    print(clean_message('campuss## life'))
    # Should print: campu life

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py
