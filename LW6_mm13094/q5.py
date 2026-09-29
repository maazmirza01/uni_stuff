# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def expand_message(encoded_message: str):
    # WRITE YOUR CODE HERE
    pos_1 = 0
    pos_2 = 0
    prev_pos_2 = -1
    decoder = ""

    for i in range(len(encoded_message)):
            if encoded_message[i] == "[":
                pos_1 = i
            elif encoded_message[i] == "]":
                pos_2 = i
            if pos_1 != 0 and pos_2 != 0:
        
                if encoded_message[pos_1 - 2] in "123456789":
                    decoder = decoder + encoded_message[prev_pos_2 + 1:pos_1 - 2] + (encoded_message[pos_1 + 1: pos_2] * int(encoded_message[pos_1 - 2:pos_1])) #+ encoded_message[pos_2+1:]
                else:
                    decoder = decoder + encoded_message[prev_pos_2+ 1:pos_1 - 1] + (encoded_message[pos_1 + 1: pos_2] * int(encoded_message[pos_1 - 1]))# + encoded_message[pos_2+1:]
                prev_pos_2 = pos_2
                pos_2 = 0
                pos_1 = 0
    decoder = decoder + encoded_message[prev_pos_2+1:]
                

    decoded_message = decoder
    return decoded_message

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

    

    print(expand_message('ab9[cd]2[ef]g'))
    # Should print: abcdcdcdcdcdcdcdcdcdefefg

    print(expand_message('3[ha]'))
    # Should print: hahaha

    print(expand_message('2[go] team!'))
    # Should print: gogo team!

    print(expand_message('2[abc]3[cd]ef'))
    # Should print: abcabccdcdcdef

    print(expand_message('12[!] done'))
    # Should print: !!!!!!!!!!!! done

    print(expand_message('3[ac]'))
    # Should print: acacac

    print(expand_message('3[a]2[bc]'))
    # Should print: aaabcbc

    print(expand_message('aa2[b]cd'))
    # Should print: aabbcd

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#
"""
FAILED tests/test_q5.py::test_q5[ab9[cd]2[ef]g-abcdcdcdcdcdcdcdcdcdefefg-True] - AssertionError: assert 'abcdcdcdcdcdcdcdcdcd2[ef]g' == 'abcdcdcdcdcdcdcdcdcdefefg'
FAILED tests/test_q5.py::test_q5[2[a]2[b]cd-aabbcd-True] - AssertionError: assert 'aa2[b]cd' == 'aabbcd'
FAILED tests/test_q5.py::test_q5[2[a]3[b]-6ea6115bab5f26516ec79af84239b082a44654ddc87c4a85af8e5b5cc1ec4a02-False] - AssertionError: assert '2d936c1d52d9...98978b8a7fb34' == '6ea6115bab5f...e5b5cc1ec4a02'
"""
# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py