# -----------------------------------------#
# FUNCTION DEFINITIONS                      #
# -----------------------------------------#

def classify_state(signature):
    # WRITE YOUR CODE HERE
    if signature % 3 == 0 and signature % 5 != 0:
        return "Stable"
    elif signature % 5 == 0 and signature % 3 != 0:
        return "Unstable"
    elif signature % 3 == 0 and signature % 5 == 0:
        return "Critical"
    else:
        return "Neutral" 

def tscore(signature, state):
    # WRITE YOUR CODE HERE
    remaining_digits = signature
    score = 0
    while True:
        last_digit = remaining_digits % 10
        remaining_digits = remaining_digits // 10
        if last_digit % 2 == 0:
            score = score + last_digit * 2
        else:
            score = score + last_digit * 3
        if remaining_digits == 0:
            break
    if state == "Crtical":
        score = score + 10
    elif state == "Stable":
        score = score - 3
    return score 
        

def next_state(signature):
    # WRITE YOUR CODE HERE
    state = classify_state(signature)
    score = tscore(signature, state)
    if state == "Critical":
        score = score + (signature//3)
    else:
        score = score + (signature//2) 
    return score

def break_loop(signature, limit):
    # WRITE YOUR CODE HERE
    temp_signature = signature
    while True:
        current_state = classify_state(temp_signature)
        current_score = tscore(temp_signature, current_state)
        if temp_signature > limit:
            return "Loop remains unbroken!"
        elif temp_signature % 7 == 0:
            return "Timeline stabilized!"
        elif 40 <= temp_signature <= 50:
            return "Intervention successful!"
        elif current_state == "Stable" and current_score >= 100:
            return "Stable state found!"
        else:
            temp_signature = next_state(temp_signature)
        
        
    


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

    print(break_loop(4, 30))
    ''' Should print:
    
    Timeline stabilized!

    '''

    print(break_loop(19, 60))
    ''' Should print:
    
    Intervention successful!

    '''

    print(break_loop(2, 25))
    ''' Should print:
   
    Loop remains unbroken!

    '''

    print(break_loop(119393, 200000))
    ''' Should print:
       
    Stable state found!
        
    '''
    
    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py
