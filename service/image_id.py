# encoding: utf-8
"""
图片ID算法
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2024-01-09
"""

__copyright__ = "Copyright (c) (2022-2024) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2024-01-09 11:44"
__version__ = "1.0.0"

import base64
import hashlib
from service.image_handel import get_image_stream
from service.image_handel import get_image_hash

# 失败特殊ID
fail_id = 18446744073709551615


def change_url(url):
    try:
        index = url.rindex('/')
        url_prefix = url[0:index]
        size = url[index + 1:]
        if url_prefix == '':
            url = ''
        elif size.isdigit():
            url = url_prefix + '/0'
    except:
        url = ''
    return url


def get_id(url, name=''):
    try:
        name_base64 = str(base64.b64encode(str(name).encode('utf-8')), "utf-8")
    except:
        name_base64 = name
    url = change_url(url)
    if url == '':
        head_id = 0
        head_size = 0
        map_str = str(head_id) + '_' + name_base64 + '_' + str(head_size)
        map_id = hashlib.md5(map_str.encode(encoding='utf-8')).hexdigest()
    else:
        try:
            image_stream = get_image_stream(url)
            head_id, head_size = get_image_hash(image_stream, (6, 7))
            map_str = str(head_id) + '_' + name_base64 + '_' + str(head_size)
            map_id = hashlib.md5(map_str.encode(encoding='utf-8')).hexdigest()
        except:
            head_id = fail_id
            head_size = 0
            map_id = ''
    return head_id, head_size, map_id


if __name__ == '__main__':
    print('check！')
    image_url = 'https://pics0.baidu.com/feed/a5c27d1ed21b0ef4c90c26e1c52c0ed783cb3e9a.jpeg@f_auto?token=587e60a994030d83b97b6f746732b2cc'
    head_id, head_size, map_id = get_id(image_url)
    print(head_id, head_size, map_id)