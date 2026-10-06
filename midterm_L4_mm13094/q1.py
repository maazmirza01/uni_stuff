# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def pikachu_status(energy):
    # WRITE YOUR CODE HERE
    if energy < 50:
        return "Low energy!"
    elif energy < 75:
        return "Energetic!"
    else:
        return "Super charged!"

def pikachu_says(energy, mood, spark):
    # WRITE YOUR CODE HERE
    energy_status = pikachu_status(energy)
    if energy_status == "Super charged!" and spark > 70:
        return "Pika Pika!"
    elif energy_status == "Energetic!" and mood > 70:
        return "Pika Chu!"
    elif energy_status == "Low energy!" and (spark > 80 or mood > 80):
        return "Pika!"
    else:
        return "Pika...?"

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

    print(pikachu_says(90, 50, 75))
    ''' Should print:
    Pika Pika!
    '''

    print(pikachu_says(70, 90, 50))
    ''' Should print:
    Pika Chu!
    '''

    print(pikachu_says(40, 50, 85))
    ''' Should print:
    Pika!
    '''

    print(pikachu_says(90, 50, 60))
    ''' Should print:
    Pika…?
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py
