#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:31:14 2018

@author: qinyuxin & hanmufu
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

margin = 0.3  # 绘图时采样点间隔

'''
已知X Y, 用开口向下的抛物面方程计算Z
para:
    X 所有采样点的x坐标的列表，np.array类型
    Y 所有采样点的y坐标的列表，np.array类型
'''

def paowumian(X, Y):
    temp = [0.0] * len(X[0])
    Z = []
    for i in range(len(X)):
        Z.append(temp)
    Z = np.array(Z)
    for i in range(len(X)):
        for j in range(len(X[i])):
            Z[i][j] = -X[i][j] ** 2 / 20 - Y[i][j] ** 2 / 20 + 12 + random.uniform(-0.7, 0.7)
    # Z = -X**2/20-Y**2/20 + 12
    return Z


'''
已知X Y, 用开口向上的锥形曲面方程计算Z
para:
    X 所有采样点的x坐标的列表，np.array类型
    Y 所有采样点的y坐标的列表，np.array类型
'''


def pingfanggen(X, Y):
    temp = [0.0] * len(X[0])
    Z = []
    for i in range(len(X)):
        Z.append(temp)
    Z = np.array(Z)
    for i in range(len(X)):
        for j in range(len(X[i])):
            Z[i][j] = np.sqrt((X[i][j]) ** 2 + (Y[i][j]) ** 2) + random.uniform(-0.7, 0.7)
    # Z = np.sqrt(X**2+Y**2)
    return Z


'''
主函数
1. 模拟垃圾状况，并绘制示意图
2. 计算垃圾真实体积，以便之后计算拟真率
'''


def main(funName):
    # 画一个关于X,Y,Z的3D图
    fig = plt.figure()
    ax = Axes3D(fig)
    # X,Y value
    X = np.arange(-12, 12, margin)
    Y = np.arange(-12, 12, margin)
    # 将X,Ymatch到底面上
    X, Y = np.meshgrid(X, Y)
    # 根据XY计算Z值
    if funName == 'pingfanggen':
        Z = pingfanggen(X, Y)
    elif funName == 'paowumian':
        Z = paowumian(X, Y)
    # rstride、csride分别为两个方向上的跨度，跨度越大越宽松，越小越密集；cmap设置为彩虹样式
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))  # 彩虹
    # 等高线图contour---细线；contourf---连在一起的宽线条 ；zdir设置从哪个坐标轴压下去;  offset=n,表示等高线图的位置在n
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
    # 设置z坐标轴的范围
    ax.set_zlim(-2, 12)
    plt.show()

    # 计算dS的面积
    truedS = 24 ** 2 / (24 / margin) ** 2
    trueVol = 0
    # 积分求体积
    for i in range(len(Z)):
        for j in range(len(Z[i])):
            trueVol += (Z[i][j] + 12) * truedS
    return trueVol


'''
情况1：一个采样点
para: 
    funName 指定曲面方程函数
    trueVol 真实体积，以便计算拟真率
'''


def sample1(funName, trueVol):
    sampleX1 = np.array([0])
    sampleY1 = np.array([0])
    sampleX1, sampleY1 = np.meshgrid(sampleX1, sampleY1)
    if funName == 'pingfanggen':
        sampleZ1 = pingfanggen(sampleX1, sampleY1)
    elif funName == 'paowumian':
        sampleZ1 = paowumian(sampleX1, sampleY1)
    else:
        print("ERROR: 所输入方程名不存在")
    sampledS1 = 24 ** 2 / 1 ** 2
    sampleVol1 = 0
    for i in range(len(sampleZ1)):
        for j in range(len(sampleZ1[i])):
            sampleVol1 += (sampleZ1[i][j] + 12) * sampledS1
    print("一个采样点的拟真率为%.3f%%, 差为%.3f%%" % (float(sampleVol1 / trueVol * 100), 100 - float(sampleVol1 / trueVol * 100)))


'''
情况2：四个采样点
para: 
    funName 指定曲面方程函数
    trueVol 真实体积，以便计算拟真率
'''


def sample4(funName, trueVol):
    sampleX2 = np.array([-4, 4])
    sampleY2 = np.array([-4, 4])
    sampleX2, sampleY2 = np.meshgrid(sampleX2, sampleY2)
    if funName == 'pingfanggen':
        sampleZ2 = pingfanggen(sampleX2, sampleY2)
    elif funName == 'paowumian':
        sampleZ2 = paowumian(sampleX2, sampleY2)
    else:
        print("ERROR: 所输入方程名不存在")
    sampledS2 = 24 ** 2 / 2 ** 2
    sampleVol2 = 0
    for i in range(len(sampleZ2)):
        for j in range(len(sampleZ2[i])):
            sampleVol2 += (sampleZ2[i][j] + 12) * sampledS2
    print("四个采样点的拟真率为%.3f%%, 差为%.3f%%" % (float(sampleVol2 / trueVol * 100), 100 - float(sampleVol2 / trueVol * 100)))


'''
情况3：九个采样点
para: 
    funName 指定曲面方程函数
    trueVol 真实体积，以便计算拟真率
'''


def sample9(funName, trueVol):
    sampleX3 = np.array([-6, 0, 6])
    sampleY3 = np.array([-6, 0, 6])
    sampleX3, sampleY3 = np.meshgrid(sampleX3, sampleY3)
    if funName == 'pingfanggen':
        sampleZ3 = pingfanggen(sampleX3, sampleY3)
    elif funName == 'paowumian':
        sampleZ3 = paowumian(sampleX3, sampleY3)
    else:
        print("ERROR: 所输入方程名不存在")
    sampledS3 = 24 ** 2 / 3 ** 2
    sampleVol3 = 0
    for i in range(len(sampleZ3)):
        for j in range(len(sampleZ3[i])):
            sampleVol3 += (sampleZ3[i][j] + 12) * sampledS3
    print("九个采样点的拟真率为%.3f%%, 差为%.3f%%" % (float(sampleVol3 / trueVol * 100), 100 - float(sampleVol3 / trueVol * 100)))


'''
情况4：十六个采样点
para: 
    funName 指定曲面方程函数
    trueVol 真实体积，以便计算拟真率
'''


def sample16(funName, trueVol):
    sampleX4 = np.array([-7.2, -2.4, 2.4, 7.2])
    sampleY4 = np.array([-7.2, -2.4, 2.4, 7.2])
    sampleX4, sampleY4 = np.meshgrid(sampleX4, sampleY4)
    if funName == 'pingfanggen':
        sampleZ4 = pingfanggen(sampleX4, sampleY4)
    elif funName == 'paowumian':
        sampleZ4 = paowumian(sampleX4, sampleY4)
    else:
        print("ERROR: 所输入方程名不存在")
    sampledS4 = 24 ** 2 / 4 ** 2
    sampleVol4 = 0
    for i in range(len(sampleZ4)):
        for j in range(len(sampleZ4[i])):
            sampleVol4 += (sampleZ4[i][j] + 12) * sampledS4
    print("十六个采样点的拟真率为%.3f%%, 差为%.3f%%" % (float(sampleVol4 / trueVol * 100), 100 - float(sampleVol4 / trueVol * 100)))


trueVol = main('pingfanggen')
sample1('pingfanggen', trueVol)
sample4('pingfanggen', trueVol)
sample9('pingfanggen', trueVol)
sample16('pingfanggen', trueVol)

main('paowumian')
sample1('paowumian', trueVol)
sample4('paowumian', trueVol)
sample9('paowumian', trueVol)
sample16('paowumian', trueVol)

