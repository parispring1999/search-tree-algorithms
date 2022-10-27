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


# 下一个queen
def jirenzhe(dz, zt):
    b = deepcopy(zt[3])
    xge = dz[0]
    yge = dz[1]
    li = list(dict.fromkeys(zt[1] + kongzhiqu(xge, yge)))
    num = len(li)
    b[yge][xge] = 1
    return num, li, (xge, yge), b


# 占用方格
def kongzhiqu(x, y):
    h = q_heng(y)
    z = q_zong(x)
    xie = q_xie(x, y)
    li = list(dict.fromkeys(h + z + xie))
    return li


def q_heng(y):
    h = []
    for x in range(xbian):
        h = h + [(x, y)]
    return h


def q_zong(x):
    z = []
    for y in range(ybian):
        z = z + [(x, y)]
    return z


def q_xie(x, y):
    na = []  # 左上到右下的斜线↘
    pie = []  # 右上到左下↙

    # 起始值
    min_na = min(x, y)
    x_na = x - min_na
    y_na = y - min_na

    x_difference = (xbian - 1) - x
    min_pie = min(x_difference, y)
    x_pie = x + min_pie
    y_pie = y - min_pie

    # 计算方格数↘和↙
    while x_na < xbian and y_na < ybian:
        na += [(x_na, y_na)]
        x_na += 1
        y_na += 1

    while x_pie >= 0 and y_pie < ybian:
        pie += [(x_pie, y_pie)]
        x_pie += -1
        y_pie += 1

    斜 = list(dict.fromkeys(na + pie))
    return 斜


def jiance(zt):
    if zt[0] == xbian * ybian:
        print("\n棋盘:")
        dayin(zt)
        return True
    return False


def dayin(zt):
    for h in zt[3]:
        for g in h:
            print("%-3i" % g, end='')
        print()


def dayinxinxi():
    print("占用", xbian, "×", ybian, "棋盘:")


# 创建一个函数把search的参数导入
def make_qc_problem(x, y):
    global xbian, ybian, chushizhi
    xbian = x
    ybian = y
    chushizhi = chushi(x, y)  # 从零开始
    return None, dayinxinxi, chushizhi, dongzuo, jirenzhe, jiance
