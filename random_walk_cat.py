# 猫的随机漫步

import numpy as np
import random

# 1. 每个数组单元初始化为0，n * m的数组，代表瓷砖被猫到达的次数
#   取n = 15, m = 15
mark = np.zeros((15, 15))
# 2. 猫在地板上的位置用坐标(currentX, currentY)表示
#   取currentX = 8, currentY = 8
currentX = 8
currentY = 8
meowCurrent = (currentX, currentY)
# 3. 猫的移动方向
# imove[0] = 0;
# jmove[0] = 1; // 正北方
# imove[1] = 1;
# jmove[1] = 1; // 东北方
# imove[2] = 1;
# jmove[2] = 0; // 正东方
# imove[3] = 1;
# jmove[3] = -1; // 东南方
# imove[4] = 0;
# jmove[4] = -1; // 正南方
# imove[5] = -1;
# jmove[5] = -1; // 西南方
# imove[6] = -1;
# jmove[6] = 0; // 正西方
# imove[7] = -1;
# jmove[7] = 1; // 西北方
# 猫的随机漫步通过一个随机数k(0<=k<=7)来模拟
imove = [0, 1, 1, 1, 0, -1, -1, -1]
jmove = [1, 1, 0, -1, -1, -1, 0, 1]
# 4. nextX = currentX + imove[k], nextY = currentY + jmove[k]
# 5. 迭代限制
num = 0
MAX = 500


# 判断是否到达过所有瓷砖
def judge_walk():
    return 0 in mark


# 随机漫步
# global声明全局变量
def random_walk():
    k = random.randint(0, 7)
    global currentX
    currentX = currentX + imove[k]
    global currentY
    currentY = currentY + jmove[k]


# 开始模拟
while judge_walk():
    num = num + 1
    if num >= MAX:
        break
    random_walk()
    while currentX > 14 or currentY > 14 or currentX < 0 or currentY < 0:
        random_walk()
    mark[currentX, currentY] = mark[currentX, currentY] + 1
    print(judge_walk())
print(mark)