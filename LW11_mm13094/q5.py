def max_positon(ticket_number):
    if ticket_number == 0:
        return -1
    else:
        return 1 + max_positon(ticket_number // 10)
        
def help_win(position, max_pos, ticket_number):
    if position == max_pos + 1:
        return True
    else:
        if position % 2 == 0:
            if (ticket_number // (10**(max_pos - position ))) % 2 == 0:
                return help_win(position +1, max_pos, ticket_number % (10**(max_pos - position)))   
            else: 
                return False
        else:
            if (ticket_number // (10**(max_pos - position))) % 2 == 1:
                return help_win(position +1, max_pos, ticket_number % (10**(max_pos - position)))   
            else: 
                return False

def is_winning_ticket(ticket_number):
    # WRITE YOUR CODE HERE
    return help_win(0, max_positon(ticket_number), ticket_number)


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

    print(is_winning_ticket(2345))
    # Should print: True

    print(is_winning_ticket(3245))
    # Should print: False

    print(is_winning_ticket(2582))
    # Should print: False

    print(is_winning_ticket(7))
    # Should print: False

    print(is_winning_ticket(2))
    # Should print: True

    print(is_winning_ticket(4101))
    # Should print: True

    print(is_winning_ticket(22))
    # Should print: False

    print(is_winning_ticket(23))
    # Should print: True

    print(is_winning_ticket(230))
    # Should print: True

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q5.py
# python3 -m pytest tests/test_q5.py
