# 包含包和模块
from __future__ import print_function
from copy import deepcopy


# 空值
def qc_get_initial_state(x, y):
    global BOARD_X, BOARD_Y, qc_initial_state
    BOARD_X = x
    BOARD_Y = y
    return 0, [], (0, 0), matrix_of_zeros(x, y)


def matrix_of_zeros(x_value, y_value):
    return [[0 for x in range(x_value)] for y in range(y_value)]


# 遍历数组和计数
def qc_possible_actions(state):
    moves = []
    for x in range(BOARD_X):
        for y in range(BOARD_Y):
            if state[3][y][x] == 0:
                moves = moves + [(x, y)]
    return moves


def qc_successor_state(action, state):
    board = deepcopy(state[3])
    x_position = action[0]
    y_position = action[1]
    control_list = list(dict.fromkeys(state[1] + controlled_squares_list(x_position, y_position)))
    control_count = len(control_list)
    board[y_position][x_position] = 1
    return control_count, control_list, (x_position, y_position), board


# 占用方格
def controlled_squares_list(x, y):
    row = queen_row(y)
    column = queen_column(x)
    diagonal = queen_diagonal(x, y)
    squares_list = list(dict.fromkeys(row + column + diagonal))  # To remove duplicate squares
    return squares_list


def queen_row(y):
    row = []
    for x in range(BOARD_X):
        row = row + [(x, y)]
    return row


def queen_column(x):
    column = []
    for y in range(BOARD_Y):
        column = column + [(x, y)]
    return column


def queen_diagonal(x, y):
    diagonal_left_right = []  # 左上到右下的斜线↘
    diagonal_right_left = []  # 右上到左下↙

    # 起始值
    min_left_right = min(x, y)
    x_left_right = x - min_left_right
    y_left_right = y - min_left_right

    x_difference = (BOARD_X - 1) - x
    min_right_left = min(x_difference, y)
    x_right_left = x + min_right_left
    y_right_left = y - min_right_left

    # 计算方格数↘和↙
    while x_left_right < BOARD_X and y_left_right < BOARD_Y:
        diagonal_left_right += [(x_left_right, y_left_right)]
        x_left_right += 1
        y_left_right += 1

    while x_right_left >= 0 and y_right_left < BOARD_Y:
        diagonal_right_left += [(x_right_left, y_right_left)]
        x_right_left += -1
        y_right_left += 1

    diagonal = list(dict.fromkeys(diagonal_left_right + diagonal_right_left))  # Remove duplicate squares
    return diagonal


def qc_test_goal_state(state):
    if state[0] == BOARD_X * BOARD_Y:
        print("\n棋盘:")
        print_board_state(state)
        return True
    return False


def print_board_state(state):
    board = state[3]
    for row in board:
        for square in row:
            print(" %2i" % square, end='')
        print()


def qc_problem_info():
    print("占用", BOARD_X, "×", BOARD_Y, "棋盘:")


def empty_squares_heuristic(state):
    return BOARD_X * BOARD_Y - state[0]


# 创建一个函数把search的参数导入
def make_qc_problem(x, y):
    global BOARD_X, BOARD_Y, qc_initial_state
    BOARD_X = x
    BOARD_Y = y
    qc_initial_state = qc_get_initial_state(x, y)  # 从零开始
    return (None,
            qc_problem_info,
            qc_initial_state,
            qc_possible_actions,
            qc_successor_state,
            qc_test_goal_state
            )
