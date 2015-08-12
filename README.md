## python_img_util

一些处理图片的python函数，包括:
- get_image_size, 获取图片长宽
- resize_img, 改变图片长宽，详见下
- is_gif,   判断是否是gif图
- gif_first_frame_to_image, 获取gif第一帧
- convert_to_webp, 将图片转为webp格式


## resize_img 的更多说明
参数
- origin_img_path, 原始图片路径
- dest_img_path， 目标图片路径，可以和原始图片路径相同。
- dest_width， 目标宽度
- dest_height， 目标高度
- resize_method, resize option， 默认为RESIZE_METHOD_MAX_RATIO
	- RESIZE_METHOD_MAX_RATIO, resize时按比例较大的边进行。例如原图尺寸为(80, 60)， 目标尺寸为（20，30）,则会先将图片resize为（40，30），然后再crop。
    - RESIZE_METHOD_MIN_RATIO，resize时按比例较小的边进行。例如原图尺寸为(80, 60)， 目标尺寸为（40，50）,则会先将图片resize为（40，30），然后再crop。
    - RESIZE_METHOD_BY_WIDTH, 按源/目的宽的比例进行resize。
    - RESIZE_METHOD_BY_HEIGHT， 按高的比例进行resize。
- crop_method
	- CROP_METHOD_NO_CROP, 不裁剪多余的部分。
    - CROP_METHOD_MIDDLE，居中裁剪。例如resize后图片为（40，40），目标尺寸为（40，30），则从裁剪后部分四个角为（0，5）,（40, 5), (0,35), (40, 35)。
    - CROP_METHOD_TOPLEFT，从左上角裁剪。


## Requirements

依赖于PIL或者Pillow, 所有代码在PIL==1.7.0和Pillow=2.9.0上验证。且需支持所操作的图片格式，例如jpeg/web等。
