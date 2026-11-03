# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def color_neighbors(tile_wall, target_color):
    # WRITE YOUR CODE HERE
    for i in range(len(tile_wall)):
        for j in range(len(tile_wall[0])):
            if tile_wall[i][j] == target_color:
                row = i
                col = j
    neighbors = []
    if col != len(tile_wall[0]) - 1:
        neighbors.append(tile_wall[row][col + 1])
    if col != 0:
        neighbors.append(tile_wall[row][col - 1])
    if row != len(tile_wall) - 1:
        neighbors.append(tile_wall[row + 1][col])
    if row != 0:
        neighbors.append(tile_wall[row - 1][col])
    return neighbors


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # sorted() displays the colors alphabetically.   #
    # ----------------------------------------------#

    tile_wall = [
        ["Red", "Blue", "Green", "Cyan"],
        ["Yellow", "Black", "White", "Brown"],
        ["Pink", "Orange", "Purple", "Gray"]
    ]

    print(sorted(color_neighbors(tile_wall, "Black")))
    # Should print: ['Blue', 'Orange', 'White', 'Yellow']

    print(sorted(color_neighbors(tile_wall, "Blue")))
    # Should print: ['Black', 'Green', 'Red']

    print(sorted(color_neighbors(tile_wall, "Gray")))
    # Should print: ['Brown', 'Purple']

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py