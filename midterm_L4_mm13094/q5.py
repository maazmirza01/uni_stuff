# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

########## Helper functions #########
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def ingredient_value(name):
    value = 0
    vowels = "aeiou"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ch in name:
        position = alphabet.index(ch) + 1
        if ch in vowels:
            value = value + (position * 2)
        else:
            value = value + position
    return value

def ingredient_score(name, quantity):
    base_value = ingredient_value(name)
    score = base_value * quantity
    if quantity > 5:
        score = score + 10
    if is_prime(quantity):
        score = score * 1.5
    return score

def total_ingredients_score(name1, quantity1, name2, quantity2):
    total = ingredient_score(name1, quantity1) + ingredient_score(name2, quantity2)
    return total

def brewing_time_label(minutes):
    if minutes < 10:
        return "Rushed"
    elif minutes <= 30:
        return "Balanced"
    elif minutes <= 60:
        return "Slow-Simmered"
    else:
        return "Overbrewed"

def brewing_time_value(minutes):
    if minutes < 10:
        return -15
    elif minutes <= 30:
        return 10
    elif minutes <= 60:
        return 25
    else:
        return -20

def magical_energy_factor(energy):
    digit_sum = 0
    n = energy
    while n > 0:
        digit_sum = digit_sum + (n % 10)
        n = n // 10
    if digit_sum % 2 == 0:
        return digit_sum * 2
    else:
        return digit_sum * 3

########## Main function ##############
def potion_power_score(name1, quantity1, name2, quantity2, brewing_time, energy):
   
    ingredient_total = total_ingredients_score(name1, quantity1, name2, quantity2)
    label = brewing_time_label(brewing_time)
    modifier = brewing_time_value(brewing_time)
    energy_factor = magical_energy_factor(energy)
    power_score = ingredient_total + energy_factor + modifier

    if power_score >= 500:
        classification = "Legendary Potion! Hogwarts takes the trophy!"
    elif power_score >= 300:
        classification = "Rare Potion - a strong contender."
    elif power_score >= 100:
        classification = "Common Potion - needs improvement."
    else:
        classification = "Failed Potion - back to the drawing board."

    print("Brewing Style: " + label)
    print("Potion Power Score: ", power_score)
    print(classification)
  

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

    potion_power_score("ivy", 1, "a", 0, 70, 3)
    ''' Should print:
  
    Brewing Style: Overbrewed
    Potion Power Score: 54
    Failed Potion - back to the drawing board.

    '''

    potion_power_score("sage", 1, "mint", 1, 15, 40)
    ''' Should print:
    
    Brewing Style: Balanced
    Potion Power Score: 121
    Common Potion - needs improvement.

    '''

    potion_power_score("sage", 2, "mint", 2, 25, 300)
    ''' Should print:
    
    Brewing Style: Balanced
    Potion Power Score: 328.0
    Rare Potion - a strong contender.

    '''

    potion_power_score("wolfsbane", 3, "moonstone", 2, 20, 487)
    ''' Should print:
    
    Brewing Style: Balanced
    Potion Power Score: 1138.0
    Legendary Potion! Hogwarts takes the trophy!

    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py
