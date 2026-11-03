# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def set_zeros(matrix: list):
    # WRITE YOUR CODE HERE
    zeroed_matrix = [row[:] for row in matrix]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                
                for a in range(len(zeroed_matrix[0])):
                    zeroed_matrix[i][a] = 0
                
                for b in range(len(zeroed_matrix)):
                    zeroed_matrix[b][j] = 0

    return zeroed_matrix


def main():
    # WRITE YOUR CODE HERE
    row, col = input().split(" ")
    row = int(row)
    matrix = []
    for i in range(row):
        matrix.append([int(num) for num in input().split(" ")])
    print(set_zeros(matrix))



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

    # Note: Inputs to be entered are labelled as [Input -> X] where X is the input.

    main()
    # [Input -> 4 5]
    # [Input -> 1 2 0 4 8]
    # [Input -> 4 5 6 5 9]
    # [Input -> 7 0 9 9 3]
    # [Input -> 9 8 7 6 2]
    # Should print: [[0, 0, 0, 0, 0], [4, 0, 0, 5, 9], [0, 0, 0, 0, 0], [9, 0, 0, 6, 2]]

    main()
    # [Input -> 3 4]
    # [Input -> 1 2 3 8]
    # [Input -> 4 5 6 9]
    # [Input -> 7 0 9 10]
    # Should print: [[1, 0, 3, 8], [4, 0, 6, 9], [0, 0, 0, 0]]

    main()
    # [Input -> 3 2]
    # [Input -> 1 0]
    # [Input -> 1 1]
    # [Input -> 3 4]
    # Should print: [[0, 0], [1, 0], [3, 0]]

    main()
    # [Input -> 4 3]
    # [Input -> 0 1 3]
    # [Input -> 1 3 6]
    # [Input -> 6 9 9]
    # [Input -> 3 7 2]
    # Should print: [[0, 0, 0], [0, 3, 6], [0, 9, 9], [0, 7, 2]]

    main()
    # [Input -> 5 4]
    # [Input -> 1 1 1 1]
    # [Input -> 5 0 4 4]
    # [Input -> 0 5 9 6]
    # [Input -> 2 0 4 1]
    # [Input -> 0 0 0 0]
    # Should print: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py
