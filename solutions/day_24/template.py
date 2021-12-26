import math
import time
from functools import cache
from itertools import product

validation = False

# w, x, y resets for each state where each state lasts 18 operations (always starting with `inp w`.
# The operations repeat themselves, with some differences in integer values (where used)
# Example:                                                                                             diff \/                                                                                                                                                                                         diff \/
# [['inp', 'w'], ['mul', 'x', '0'], ['add', 'x', 'z'], ['mod', 'x', '26'], ['div', 'z', '1'], ['add', 'x', '11'], ['eql', 'x', 'w'], ['eql', 'x', '0'], ['mul', 'y', '0'], ['add', 'y', '25'], ['mul', 'y', 'x'], ['add', 'y', '1'], ['mul', 'z', 'y'], ['mul', 'y', '0'], ['add', 'y', 'w'], ['add', 'y', '14'], ['mul', 'y', 'x'], ['add', 'z', 'y']]
# [['inp', 'w'], ['mul', 'x', '0'], ['add', 'x', 'z'], ['mod', 'x', '26'], ['div', 'z', '1'], ['add', 'x', '14'], ['eql', 'x', 'w'], ['eql', 'x', '0'], ['mul', 'y', '0'], ['add', 'y', '25'], ['mul', 'y', 'x'], ['add', 'y', '1'], ['mul', 'z', 'y'], ['mul', 'y', '0'], ['add', 'y', 'w'], ['add', 'y', '6'], ['mul', 'y', 'x'], ['add', 'z', 'y']]
# Sometimes the 5th operation is a division of z with 26, then the next add x operation has a negative integer
# [['inp', 'w'], ['mul', 'x', '0'], ['add', 'x', 'z'], ['mod', 'x', '26'], ['div', 'z', '26'], ['add', 'x', '-12'], ['eql', 'x', 'w'], ['eql', 'x', '0'], ['mul', 'y', '0'], ['add', 'y', '25'], ['mul', 'y', 'x'], ['add', 'y', '1'], ['mul', 'z', 'y'], ['mul', 'y', '0'], ['add', 'y', 'w'], ['add', 'y', '8'], ['mul', 'y', 'x'], ['add', 'z', 'y']]

# So there's two parts to each state of operations
# The first is x
    # Set x to 0
    # Add previous z state to x
    # Divide z by either 1 or 26 and put the remainder in x
    # If z was divided by 26, add a negative value to x, else a positive value
        # Lets call this value ADD_X
    # Check if x is equal to w, then set x to 0, else 1
# The second is y
    # If x is equal to w, set y to 0, else 25
    # Add 1 to y (Either 26 or 1)
    # Multiply z with y (i.e. z = z * 26 or z = z)
    # Set y to w
    # Add some value to y
        # Let's call this value ADD_Y
    # Multiply y by x
    # Add y to z
# Done

# Looking at the second part of the operations we can see that z is only altered if x is not equal to w, i.e.
# If x is equal to w
    # z = z * 26 + w + ADD_Y
# Done

# What varies for each state?
# Z varies, and the values added to X and Y varies, i.e. for each state we could cache these results

# Take the idea with "universes" and apply here, for each number in a possible model number, expand with 10 new
#  universes and do so for each model number character until we have found all possible model numbers

# It takes forever to solve this even when using caches in the recursive functions (~10^14 different possibilities?)
# Can we constrain searches somehow? Any early returns?
# z is always divided by either 1 or 26, so in order for z to reach 1 the value has to be less than or equal to
#  26^(number_of_26_divisions_left) for each state
# This early return was enough

# Finding all solutions take ~4.5s
# Finding only first and last take ~1.8s
# Interestingly, caching the results of calc_z increases the execution time by about 50% ~1.2s -> ~1.8s
# I suppose the lookup + memory grabbing takes more time than the actual execution.

time_start = time.perf_counter()
with open("input.txt", "r") as file:

    #@cache
    def calc_z(z, w, m_n_pos):
        x = (z % 26) + ADD_X[m_n_pos]
        z /= DIV_Z[m_n_pos]
        if z > 0:
            z = int(math.floor(z))
        else:
            z = int(math.ceil(z))

        if x != w:
            z = z * 26 + w + ADD_Y[m_n_pos]

        return z


    @cache
    def find_first_possible_model_num(curr_z, m_n_pos):
        string = ""

        if curr_z > MAX_Z[m_n_pos]:
            return string

        for w in possible_numbers:
            next_z = calc_z(curr_z, w, m_n_pos)
            # If we're at the last number in the model number
            if m_n_pos == 13:
                # Check if the model number is correct (last z == 0)
                if next_z == 0:
                    # Then return
                    return str(w)
            else:
                num = find_first_possible_model_num(next_z, m_n_pos + 1)
                if len(num) > 0:
                    return ''.join([str(w), num])

        return string


    operations = [operation.split(' ') for operation in file.read().split('\n')]
    ADD_X = []
    ADD_Y = []
    DIV_Z = []
    # There's 14 repeats of operations
    for i in range(14):
        # Operations repeat every 18th line
        operation_state = operations[i*18: (i+1)*18]
        DIV_Z.append(int(operation_state[4][2]))
        ADD_X.append(int(operation_state[5][2]))
        ADD_Y.append(int(operation_state[15][2]))
    print(f'{ADD_X=}')
    print(f'{ADD_Y=}')
    print(f'{DIV_Z=}')

    MAX_Z = []
    for i in range(len(DIV_Z)):
        num_26_divs = 0
        for j in range(i, len(DIV_Z)):
            if DIV_Z[j] == 26:
                num_26_divs += 1
        MAX_Z.append(26 ** num_26_divs)

    print(f'{MAX_Z=}')

    # Check numbers highest to lowest
    possible_numbers = range(9, 0, -1)
    highest_possible_model_number = find_first_possible_model_num(0, 0)

    # Check numbers lowest to highest
    find_first_possible_model_num.cache_clear()
    possible_numbers = range(1, 10)
    lowest_possible_model_number = find_first_possible_model_num(0, 0)

    answer_part_1 = highest_possible_model_number
    answer_part_2 = lowest_possible_model_number
    print(f'{answer_part_1=} {answer_part_2=}')
    assert (answer_part_1 == "45989929946199" and answer_part_2 == "11912814611156")


print(f'Execution time was {time.perf_counter() - time_start} seconds')
