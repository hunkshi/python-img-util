#!/usr/bin/python
# -*- coding:utf8 -*-

from PIL import Image
import imghdr
import os


RESIZE_METHOD_MAX_RATIO = 1
RESIZE_METHOD_MIN_RATIO = 2
RESIZE_METHOD_BY_WIDTH = 3
RESIZE_METHOD_BY_HEIGHT = 4


CROP_METHOD_NO_CROP = 0
CROP_METHOD_MIDDLE = 1
CROP_METHOD_TOPLEFT = 2

DEFAULT_QUALITY = 75


def get_image_size(path):
    try:
        return True, Image.open(path, 'r').size
    except Exception as e:
        return False, 'get_img_size, error, %s, %s' % (path, e)


def resize_img(
        origin_img_path, dest_img_path,
        dest_width, dest_height,
        resize_method=RESIZE_METHOD_MAX_RATIO,
        crop_method=CROP_METHOD_MIDDLE,
        quality=DEFAULT_QUALITY):
    try:
        img = Image.open(origin_img_path)
    except Exception as e:
        return False, 'load image error, %s, %s' % (origin_img_path, e)

    origin_w, origin_h = img.size
    if (origin_w, origin_h) == (dest_width, dest_height):
        return True, ''

    new_width, new_height = get_dest_size(origin_w, origin_h, dest_width, dest_height, resize_method)

    try:
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
    except Exception as e:
        return False, 'resize image error, %s, %s' % (origin_img_path, e)

    if crop_method != CROP_METHOD_NO_CROP and (new_width > dest_width or new_height > dest_height):
        try:
            box = get_crop_box(new_width, new_height, dest_width, dest_height, crop_method)
            new_im = img.crop(box)
            new_im.save(dest_img_path, quality=quality)
        except Exception as e:
            return False, 'crop error! %s, %s' % (origin_img_path, e)
    else:
        img.save(dest_img_path, quality=quality)

    return True, 'ok'


def get_dest_size(origin_w, origin_h, dest_w, dest_h, resize_method):
    w_ratio = float(dest_w) / origin_w
    h_ratio = float(dest_h) / origin_h
    if resize_method == RESIZE_METHOD_MAX_RATIO:
        ratio = max(w_ratio, h_ratio)
    elif resize_method == RESIZE_METHOD_MIN_RATIO:
        ratio = min(w_ratio, h_ratio)
    elif resize_method == RESIZE_METHOD_BY_WIDTH:
        ratio = w_ratio
    elif resize_method == RESIZE_METHOD_BY_HEIGHT:
        ratio = h_ratio
    return int(origin_w * ratio), int(origin_h * ratio)


def get_crop_box(origin_w, origin_h, dest_w, dest_h, crop_method):
    if crop_method == CROP_METHOD_MIDDLE:
        x_cut = (origin_w - dest_w) / 2
        y_cut = (origin_h - dest_h) / 2
        return (x_cut, y_cut, x_cut + dest_w, y_cut + dest_h)
    elif crop_method == CROP_METHOD_TOPLEFT:
        return (0, 0, dest_w, dest_h)


def is_gif(img_path):
    return imghdr.what(img_path) == 'gif'


def gif_first_frame_to_image(gif_file, dest_file_name='', quality=DEFAULT_QUALITY):
    try:
        dest_dir = os.path.dirname(gif_file)
        if not dest_file_name:
            basename = os.path.basename(gif_file)
            file_name = basename[:basename.rfind('.')]
            dest_file_name = '%s_preview.jpeg' % file_name

        im = Image.open(gif_file)
        palette = im.getpalette()
        im.putpalette(palette)
        new_im = Image.new('RGB', im.size, (255, 255, 255))
        new_im.paste(im)
        new_im.save(os.path.join(dest_dir, dest_file_name), 'JPEG', quality=DEFAULT_QUALITY)
        return True, dest_file_name
    except Exception as e:
        return False, 'gif_first_frame_to_image error, %s' % e


def convert_to_webp(src, remove_origin=True):
    try:
        img = Image.open(src).convert("RGB")
        dest_dir = os.path.dirname(src)
        basename = os.path.basename(src)
        file_name = basename[:basename.rfind('.')]
        dest_file_name = '%s.webp' % file_name
        img.save(os.path.join(dest_dir, dest_file_name), 'WEBP')
        if remove_origin:
            os.remove(src)
        return True, dest_file_name
    except Exception as e:
        return False, 'convert_to_webp error, %s' % e
