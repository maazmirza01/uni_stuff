# -----------------------------------------#
# FUNCTION DEFINITIONS                      #
# -----------------------------------------#

def get_letter(c1, c2):
    # WRITE YOUR CODE HERE
    ascii_c1 = ord(c1)
    ascii_c2 = ord(c2)
    return chr(ascii_c1 + ascii_c2)
    

def convert_message(message):
    # WRITE YOUR CODE HERE
    new_message = ""
    index = 1
    length = len(message)
    while index < length:
        rep_letter = get_letter(message[index-1], message[index])
        new_message = new_message + rep_letter
        index += 2
    return new_message


def swap_halves(message):
    # WRITE YOUR CODE HERE
    length = len(message)
    new_message = message[length//2:] + message[:length//2]
    return new_message

def reverse_string(message):
    # WRITE YOUR CODE HERE
    return message[::-1]

def change_symbols(message):
    # WRITE YOUR CODE HERE
    for i in range(len(message)):
        if not (message[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtsuvwxyz"):
            message = message[:i] + " " + message[i+1:]
    return message

def decipher_text(message):
    # WRITE YOUR CODE HERE
    converted_message = convert_message(message)
    swapped_message = swap_halves(converted_message)
    reversed_message = reverse_string(swapped_message)
    deciphered_text = change_symbols(reversed_message)
    return deciphered_text

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

    print(decipher_text("7<@4$?!@(>-<@42@!@??'>+=@47<-<2@!@6:??4:-<??'>-<1;??"))
    ''' Should print:
        
    the artifacts lie in paris
    
    '''

    print(decipher_text("-<??'>%?-<+='>3:/@2@??4:"))
    ''' Should print:
    
    hide in rome

    '''

    print(decipher_text("@4??'>8>!@7<@42@!@??'>+="))
    ''' Should print:
    
    save the art

    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py
