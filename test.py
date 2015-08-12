#!/usr/bin/python
# -*- coding:utf8 -*-


from python_img_util import *


def main():
    # test_resize()
    # test_is_gif()
    test_gif_first_frame_to_image()
    # test_convert_to_webp()


def test_resize():
    src_img = 'img/test.jpg'
    w = 80
    h = 160
    resize_method = RESIZE_METHOD_BY_HEIGHT
    crop_method = CROP_METHOD_NO_CROP
    dest_img = os.path.join('img/', 'resize_%d_%d_%d_%d.jpg' % (w, h, resize_method, crop_method))
    print dest_img
    success, msg = resize_img(src_img, dest_img, w, h, resize_method, crop_method)
    print success, msg


def test_is_gif():
    print is_gif('img/test.jpg')
    print is_gif('img/test.gif')


def test_gif_first_frame_to_image():
    src_img = 'img/test.gif'
    success, msg = gif_first_frame_to_image(src_img)


def test_convert_to_webp():
    src_img = 'img/test.jpg'
    success, msg = convert_to_webp(src_img, False)
    print success, msg


main()
