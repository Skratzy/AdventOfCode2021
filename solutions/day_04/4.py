validation = False


def find_winning_board_index(boards, boards_column_based, draw_numbers):
    drawn_numbers = []
    for curr_drawn_number in draw_numbers:
        drawn_numbers.append(curr_drawn_number)
        for board_index, board in enumerate(boards):
            for board_line in board:
                all_in_drawn_numbers = True
                for board_line_num in board_line:
                    if board_line_num not in drawn_numbers:
                        all_in_drawn_numbers = False
                        break
                if all_in_drawn_numbers:
                    return drawn_numbers, int(curr_drawn_number), board_index

            for board_line in boards[board_index]:
                all_in_drawn_numbers = True
                for board_line_num in board_line:
                    if board_line_num not in drawn_numbers:
                        all_in_drawn_numbers = False
                        break
                if all_in_drawn_numbers:
                    return drawn_numbers, int(curr_drawn_number), board_index


def part_1():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        draw_numbers = file.readline().strip().split(',')
        _ = file.readline()

        boards = [board_line.split('\n') for board_line in file.read().split('\n\n')]
        for board_index, board in enumerate(boards):
            for board_line_index, board_line in enumerate(board):
                boards[board_index][board_line_index] = board_line.split()

        num_columns = len(boards[0][0])
        boards_column_based = []
        for board_index, board in enumerate(boards):
            boards_column_based.append([])
            for column_index in range(num_columns):
                boards_column_based[board_index].append([])
                for board_line in board:
                    boards_column_based[board_index][column_index].append(board_line[column_index])

        drawn_numbers, final_num, winning_board_index = find_winning_board_index(boards, boards_column_based, draw_numbers)

        sum_of_undrawn_nums = 0
        for board_line in boards[winning_board_index]:
            for board_num in board_line:
                if board_num not in drawn_numbers:
                    sum_of_undrawn_nums += int(board_num)

        return sum_of_undrawn_nums * final_num


def find_last_winning_board_index(boards, boards_column_based, draw_numbers):
    drawn_numbers = []
    won_boards = []
    drawn_numbers_when_last_board_won = []
    final_drawn_num = 0
    for curr_drawn_number in draw_numbers:
        drawn_numbers.append(curr_drawn_number)
        for board_index, board in enumerate(boards):
            if board_index not in won_boards:
                for board_line in board:
                    all_in_drawn_numbers = True
                    for board_line_num in board_line:
                        if board_line_num not in drawn_numbers:
                            all_in_drawn_numbers = False
                            break
                    if all_in_drawn_numbers:
                        final_drawn_num = int(curr_drawn_number)
                        won_boards.append(board_index)
                        drawn_numbers_when_last_board_won = list(drawn_numbers)

                for board_line in boards_column_based[board_index]:
                    all_in_drawn_numbers = True
                    for board_line_num in board_line:
                        if board_line_num not in drawn_numbers:
                            all_in_drawn_numbers = False
                            break
                    if all_in_drawn_numbers:
                        final_drawn_num = int(curr_drawn_number)
                        won_boards.append(board_index)
                        drawn_numbers_when_last_board_won = list(drawn_numbers)

    return won_boards[-1], final_drawn_num, drawn_numbers_when_last_board_won


def part_2():
    part_2_input_file = "input.txt"
    if validation:
        part_2_input_file = "validation_part_2.txt"
    with open(part_2_input_file, "r") as file:
        # Solution here
        draw_numbers = file.readline().strip().split(',')
        _ = file.readline()

        boards = [board_line.split('\n') for board_line in file.read().split('\n\n')]
        for board_index, board in enumerate(boards):
            for board_line_index, board_line in enumerate(board):
                boards[board_index][board_line_index] = board_line.split()

        num_columns = len(boards[0][0])
        boards_column_based = []
        for board_index, board in enumerate(boards):
            boards_column_based.append([])
            for column_index in range(num_columns):
                boards_column_based[board_index].append([])
                for board_line in board:
                    boards_column_based[board_index][column_index].append(board_line[column_index])

        last_won_board_index, final_drawn_num, drawn_numbers_when_last_board_won = find_last_winning_board_index(boards, boards_column_based, draw_numbers)

        sum_of_undrawn_nums = 0
        for board_line in boards[last_won_board_index]:
            for board_num in board_line:
                if board_num not in drawn_numbers_when_last_board_won:
                    sum_of_undrawn_nums += int(board_num)

        return sum_of_undrawn_nums * final_drawn_num


answer_part_1 = part_1()
answer_part_2 = part_2()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 55770 and answer_part_2 == 2980)
