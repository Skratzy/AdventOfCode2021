from functools import cache

validation = False


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        player_1_pos, player_2_pos = file.read().split('\n')
        _, player_1_pos = player_1_pos.split(': ')
        player_1_pos = int(player_1_pos)
        _, player_2_pos = player_2_pos.split(': ')
        player_2_pos = int(player_2_pos)
        #print(player_1_pos, player_2_pos)

        deterministic_die = 0
        scores = [0, 0]
        number_of_rolls = 0
        while scores[0] < 1000 and scores[1] < 1000:
            roll = 0
            for i in range(3):
                deterministic_die += 1
                if deterministic_die > 100:
                    deterministic_die -= 100
                roll += deterministic_die
                #print(deterministic_die)
            number_of_rolls += 3
            player_1_pos += roll
            while player_1_pos > 10:
                player_1_pos -= 10
            scores[0] += player_1_pos
            #print(f'{player_1_pos=}')

            if scores[0] < 1000:
                roll = 0
                for i in range(3):
                    deterministic_die += 1
                    if deterministic_die > 100:
                        deterministic_die -= 100
                    roll += deterministic_die
                    #print(deterministic_die)
                number_of_rolls += 3
                player_2_pos += roll
                #print(f'{player_2_pos=}')
                while player_2_pos > 10:
                    player_2_pos -= 10
                scores[1] += player_2_pos
                #print(f'{player_2_pos=}')

            #print(scores)


        return min(scores) * number_of_rolls


# player_1 and player_2 pos will be interchangeable, every other call they will switch place
# can't send a list of scores or positions since they are mutable
@cache
def wins(player_1_pos, player_2_pos, player_1_score, player_2_score):

    if player_1_score > 20:
        return [1, 0]
    elif player_2_score > 20:
        return [0, 1]

    # 3 possible outcomes for each die, roll 3 times for each player
    win_count = [0, 0]
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                # Current universe
                player_1_curr_pos = player_1_pos + i + j + k
                while player_1_curr_pos > 10:
                    player_1_curr_pos -= 10
                player_1_curr_score = player_1_score + player_1_curr_pos

                next_win_count = wins(player_2_pos, player_1_curr_pos, player_2_score, player_1_curr_score)
                win_count[0] += next_win_count[1]
                win_count[1] += next_win_count[0]

    return win_count


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        player_1_pos, player_2_pos = file.read().split('\n')
        _, player_1_pos = player_1_pos.split(': ')
        player_1_pos = int(player_1_pos)
        _, player_2_pos = player_2_pos.split(': ')
        player_2_pos = int(player_2_pos)

        tot_wins = wins(player_1_pos, player_2_pos, 0, 0)
        #print(tot_wins)

        return max(tot_wins)


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 906093 and answer_part_2 == 274291038026362)
