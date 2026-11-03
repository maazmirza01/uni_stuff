def help_hours_cal(time_list, task_hours, member_count, current_member):
    if task_hours[0:] == []:
        return time_list
    else:
        time_list[current_member] += task_hours[0]
        if current_member == member_count -1:
            current_member = -1
        return help_hours_cal(time_list, task_hours[1:], member_count, current_member + 1)
    
def hours_per_member(task_hours, member_count):
    # WRITE YOUR CODE HERE
    time_list = [0] * member_count
    return help_hours_cal(time_list, task_hours, member_count, 0)


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

    print(hours_per_member([1, 2, 3, 4, 5], 2))
    # Should print: [9, 6]

    print(hours_per_member([1, 2, 3, 4, 5], 3))
    # Should print: [5, 7, 3]

    print(hours_per_member([1, 2, 3], 5))
    # Should print: [1, 2, 3, 0, 0]

    print(hours_per_member([], 3))
    # Should print: [0, 0, 0]

    print(hours_per_member([4, 5, 6, 7], 1))
    # Should print: [22]

    print(hours_per_member([3] * 300, 4))
    # Should print: [225, 225, 225, 225]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py
