# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

########## Helper functions #########
def has_accepted_length(s):
    return 8 < len(s) < 30

def has_uppercase(s):
    for i in s:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return True
    return False

def has_lowercase(s):
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            return True
    return False

def has_digit(s):
    for c in s:
        if c in '0123456789':
            return True
    return False

def has_space(s):
    return ' ' in s

def get_error(n):
    message = ''
    if n == 1:
        message = 'Length must be between 8 and 30 characters (exclusive).'
    elif n == 2:
        message = 'There must be at least one upper case character.'
    elif n == 3:
        message = 'There must be at least one lower case character.'
    elif n == 4:
        message = 'There must be at least one digit.'
    elif n == 5:
        message = 'There must be no spaces in the password.'
    elif n == 0:
        message = 'Strong Password!'
    return message

########## Main function ##############
def check_password_strength(password):
    message = ''
    if not has_accepted_length(password):
        message = get_error(1)
    elif not has_uppercase(password):
        message = get_error(2)
    elif not has_lowercase(password):
        message = get_error(3)
    elif not has_digit(password):
        message = get_error(4)
    elif has_space(password):
        message = get_error(5)
    else:
        message = get_error(0)
    print(message)

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

    check_password_strength('sd2j42n 35')
    # Should print: There must be at least one upper case character.
     
    check_password_strength('ASO3QSA')
    # Should print: Length must be between 8 and 30 characters (exclusive).
     
    check_password_strength('StrongPass9')
    # Should print: Strong Password!

    check_password_strength('ABCDEFGHIJ')
    # Should print: There must be at least one lower case character.

    check_password_strength('A1b2C3d45FS')
    # Should print: Strong Password!

    check_password_strength('Abc123 45')
    # Should print: There must be no spaces in the password.

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py