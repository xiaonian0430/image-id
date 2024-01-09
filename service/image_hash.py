# encoding: utf-8
"""
图片hash处理
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2022-09-08
"""

__copyright__ = "Copyright (c) (2022-2022) QF Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2022-09-10:14:13:24"
__version__ = "1.0.0"

import cv2
import numpy as np


def average_hash(image_code, shape=(8, 8)):
    """
    均值hash算法
    """

    # 缩放
    image_resize = cv2.resize(image_code, shape)

    # 转换为灰度图

    image_gray_value = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    # 求平均灰度
    avg = np.mean(image_gray_value)

    # 灰度大于平均值为1相反为0生成图片的hash值
    same_num = 0
    for i in range(shape[1]):
        for j in range(shape[0]):
            if image_gray_value[i, j] > avg:
                hash_str = hash_str + '1'
            elif image_gray_value[i, j] == avg:
                hash_str = hash_str + '0'
                same_num = same_num + 1
            else:
                hash_str = hash_str + '0'
    return hash_str, same_num, image_gray_value[0][0]