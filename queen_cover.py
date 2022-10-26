# 包含包和模块
from __future__ import print_function
from copy import deepcopy


# 空值
def chushi(x, y):
    global xbian, ybian, chushizhi
    xbian = x
    ybian = y
    return 0, [], (0, 0), ling(x, y)


def ling(x1, y1):
    return [[0 for x in range(x1)] for y in range(y1)]


# 遍历数组和计数
def dongzuo(zt):
    yd = []
    for x in range(xbian):
        for y in range(ybian):
            if zt[3][y][x] == 0:
                yd = yd + [(x, y)]
    return yd


def jiren(dz, zt):
    board = deepcopy(zt[3])
    x_position = dz[0]
    y_position = dz[1]
    control_list = list(dict.fromkeys(zt[1] + controlled_squares_list(x_position, y_position)))
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
    for x in range(xbian):
        row = row + [(x, y)]
    return row


def queen_column(x):
    column = []
    for y in range(ybian):
        column = column + [(x, y)]
    return column


def queen_diagonal(x, y):
    diagonal_left_right = []  # 左上到右下的斜线↘
    diagonal_right_left = []  # 右上到左下↙

    # 起始值
    min_left_right = min(x, y)
    x_left_right = x - min_left_right
    y_left_right = y - min_left_right

    x_difference = (xbian - 1) - x
    min_right_left = min(x_difference, y)
    x_right_left = x + min_right_left
    y_right_left = y - min_right_left

    # 计算方格数↘和↙
    while x_left_right < xbian and y_left_right < ybian:
        diagonal_left_right += [(x_left_right, y_left_right)]
        x_left_right += 1
        y_left_right += 1

    while x_right_left >= 0 and y_right_left < ybian:
        diagonal_right_left += [(x_right_left, y_right_left)]
        x_right_left += -1
        y_right_left += 1

    diagonal = list(dict.fromkeys(diagonal_left_right + diagonal_right_left))  # Remove duplicate squares
    return diagonal


def qc_test_goal_state(state):
    if state[0] == xbian * ybian:
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
    print("占用", xbian, "×", ybian, "棋盘:")


def empty_squares_heuristic(state):
    return xbian * ybian - state[0]


# 创建一个函数把search的参数导入
def make_qc_problem(x, y):
    global xbian, ybian, chushizhi
    xbian = x
    ybian = y
    chushizhi = chushi(x, y)  # 从零开始
    return (None,
            qc_problem_info,
            chushizhi,
            dongzuo,
            jiren,
            qc_test_goal_state
            )
