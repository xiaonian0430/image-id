# encoding: utf-8
"""
图片处理
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2024-01-09 11:00
"""

__copyright__ = "Copyright (c) (2022-2024) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2024-01-09 11:16:24"
__version__ = "1.0.0"

from my_fake_useragent import UserAgent
import requests
import numpy as np
import cv2
from service.image_hash import average_hash


"""空白图片图片"""
one_color_id = 18446744073709551000


def get_image_stream(image_url):
    """
    获取在线图片流数据
    """
    ua = UserAgent(family='chrome')
    headers = {"User-Agent": ua.random()}
    response = requests.request(
        method='GET',
        url=image_url,
        headers=headers,
        stream=True)
    if response.status_code == 200:
        return response.content
    else:
        return ''


def get_image_hash(image_stream, shape):
    image_array = np.asarray(bytearray(image_stream), dtype="uint8")
    image_code = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    head_binary, same_num, same_value = average_hash(image_code, shape)
    np_size = shape[0] * shape[1]
    if np_size == same_num:
        head_id = same_value + one_color_id
        head_size = same_value
    else:
        head_id = int(head_binary, 2)
        if head_id < 1:
            head_id = 1
        head_size = round(np.sum(image_array) / 10000000)
        if head_size < 1:
            head_size = 1
    return head_id, head_size


if __name__ == '__main__':
    print('check！')
    image_url = 'https://pics0.baidu.com/feed/a5c27d1ed21b0ef4c90c26e1c52c0ed783cb3e9a.jpeg@f_auto?token=587e60a994030d83b97b6f746732b2cc'
    stream = get_image_stream(image_url)
    head_id, head_size = get_image_hash(stream, (6, 7))
    print(head_id, ',', head_size)
