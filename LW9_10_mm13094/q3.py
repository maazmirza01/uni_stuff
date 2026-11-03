# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def count_solo_invigilators(hall_layout):
    # WRITE YOUR CODE HERE
    sum = 0
    for i in range(len(hall_layout)):
        count = 0
        for item_pos in range(len(hall_layout[i])):
            if hall_layout[i][item_pos] == "I":
                invig_pos = item_pos
                count += 1
        if count == 1:
            col_count = 0
            for j in range(len(hall_layout)):
                if hall_layout[j][invig_pos] == "I":
                    col_count += 1
            if col_count == 1:
                sum += 1 
            
    return sum


def main():
    # WRITE YOUR CODE HERE
    row, col = input().split(" ")
    row = int(row)
    col = int(col)
    hall_layout = []
    for i in range(row):
        hall_layout.append(input().split(" "))
    print(count_solo_invigilators(hall_layout))


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

    main()
    # [ Input -> 3 4 ]
    # [ Input -> I E E E ]
    # [ Input -> E E I E ]
    # [ Input -> E I E E ]
    # Should print: 3

    main()
    # [ Input -> 3 4 ]
    # [ Input -> I I E E ]
    # [ Input -> E E I E ]
    # [ Input -> E E E I ]
    # Should print: 2

    main()
    # [ Input -> 3 3 ]
    # [ Input -> I I E ]
    # [ Input -> I I E ]
    # [ Input -> E E E ]
    # Should print: 0

    main()
    # [ Input -> 3 3 ]
    # [ Input -> I E E ]
    # [ Input -> E E I ]
    # [ Input -> E I E ]
    # Should print: 3

    main()
    # [ Input -> 3 3 ]
    # [ Input -> I E I ]
    # [ Input -> E I E ]
    # [ Input -> I E E ]
    # Should print: 1

    main()
    # [ Input -> 2 3 ]
    # [ Input -> E E E ]
    # [ Input -> E E E ]
    # Should print: 0

    main()
    # [ Input -> 4 4 ]
    # [ Input -> I E E E ]
    # [ Input -> E E I E ]
    # [ Input -> E I E E ]
    # [ Input -> E E E I ]
    # Should print: 4

    main()
    # [ Input -> 3 2 ]
    # [ Input -> I E ]
    # [ Input -> I E ]
    # [ Input -> E I ]
    # Should print: 1

    main()
    # [ Input -> 1 1 ]
    # [ Input -> I ]
    # Should print: 1

    main()
    # [ Input -> 1 5 ]
    # [ Input -> I I I I I ]
    # Should print: 0

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q3.py
# python3 -m pytest tests/test_q3.py