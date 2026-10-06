

# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#
def give_odd(num):
    nth = 0
    count = -1
    if num == 0:
        return 0
    while True:
        nth += 1
        count += 2

        if nth == num:
            break
    return count
def dorothy_hourglass(n):
    # WRITE YOUR CODE HERE
    if n < 1 or n > 10:
        print("n is out of range!")
    else:
        symbols = "*+?$#-@~=^"
        max_odd = give_odd(n)
        for i in range(n, 0, -1):
            for space1 in range(0, (max_odd - give_odd(i))//2):
                print(" ", end="")
            for j in range(give_odd(i)):
                print(symbols[n - i], end="")
            print()
        for k in range(1, n):
            for space2 in range(0, (max_odd - give_odd(k + 1))//2):
                print(" ", end="")
            for j in range(give_odd(k + 1)):
                print(symbols[n - k - 1], end="")
            print()
            

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

    dorothy_hourglass(5)
    ''' Should print:
        *********
         +++++++
          ?????
           $$$
            #
           $$$
          ?????
         +++++++
        *********
    '''

    dorothy_hourglass(1)
    ''' Should print:
        *
    '''

    dorothy_hourglass(10)
    ''' Should print:
        *******************
         +++++++++++++++++
          ???????????????
           $$$$$$$$$$$$$
            ###########
             ---------
              @@@@@@@
               ~~~~~
                ===
                 ^
                ===
               ~~~~~
              @@@@@@@
             ---------
            ###########
           $$$$$$$$$$$$$
          ???????????????
         +++++++++++++++++
        *******************
    '''

    dorothy_hourglass(12)
    ''' Should print:
        n is out of range!    
    '''
    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q2.py
