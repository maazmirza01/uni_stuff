# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def clean_walkway(walkway):
    # WRITE YOUR CODE HERE
    left = ""
    right = ""
    for i in range(0, len(walkway)):
        if i > 0:
            left = walkway[i - 1]
        if i < len(walkway) - 1:
            right = walkway[i + 1]
        if walkway[i] == "V":
            if right == "L":
                walkway = walkway[:i + 1] + "E" + walkway[i + 2:]
                right = ""
            elif left == "L":
                walkway = walkway[:i - 1] + "E" + walkway[i:]
                left = ""
        
    return walkway
         




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

    print(clean_walkway('LVLEL'))
    # Should print: LVEEL
     
    print(clean_walkway('VLLVE'))
    # Should print: VEEVE

    print(clean_walkway("LLLLL"))
    # Should print: LLLLL

    print(clean_walkway("VVVV"))
    # Should print: VVVV

    print(clean_walkway("LVLVLV"))
    # Should print: LVEVEV

    print(clean_walkway("LLLV"))
    # Should print: LLEV

    print(clean_walkway("VLLL"))
    # Should print: VELL

    print(clean_walkway("LVLELVLEVL"))
    # Should print: LVEELVEEVE

    print(clean_walkway("LLLLLVVVVV"))
    # Should print: LLLLEVVVVV

    print(clean_walkway("EVVEVLELV"))
    # Should print: EVVEVEEEV

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py