# encoding: utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2024-01-08
"""
__copyright__ = "Copyright (c) (2022-2024) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2024-01-09 11:54:24"
__version__ = "1.0.0"
from service.image_id import get_id

if __name__ == '__main__':
    print('>> 程序加载完成！')

    image_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202005%2F07%2F20200507184355_By5mf.thumb.1000_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1707365092&t=460f6de0a3b5b104b20a19307f29a8e4'
    head_id, head_size, map_id = get_id(image_url)
    print(head_id, head_size, map_id)

    image_url = 'https://p6.itc.cn/q_70/images03/20201003/8b4aaa0a17e548acb471ace53cfe7570.jpeg'
    head_id, head_size, map_id = get_id(image_url)
    print(head_id, head_size, map_id)
