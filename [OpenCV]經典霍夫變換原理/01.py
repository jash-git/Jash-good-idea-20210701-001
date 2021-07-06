import os
import re
import cv2
import numpy as np


# 初始化一个掩膜
def mask_create():
    img = cv2.imread('0.png')
    zero = np.zeros_like(img[:, :, 0])
    poly = np.array([[50, 270], [220, 160], [345, 160], [480, 270]])
    zero_fixed = cv2.fillConvexPoly(zero, poly, (255, 255, 255))
    return zero_fixed

# 掩膜计算，传入的图像需要是BGR图
def mask_calc(frame, mask):
    img = cv2.bitwise_and(frame[:, :, 0], frame[:, :, 0], mask=mask)
    return img

# 图像阈值操作，传入的图片需要是灰度图
def threshold(low, high, img):
    ret, thresh = cv2.threshold(img, low, high, cv2.THRESH_BINARY)
    return thresh

# 对图像进行霍夫变换，输入的图像需要是二值图,距离r为1,旋转角为1度,投票阈值为30,最远距离为200像素
# 并在原图上进行绘制图像
def hough(thresh, img):
    lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)
    try:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            img = cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
    except:
        return img
    else:
        return img
# 主函数
def mainn():
    # 读取数据
    col_frames = os.listdir('../frames/')
    # 排序
    col_frames.sort(key=lambda f: int(re.sub('\D', '', f)))
    # 读取画面每一帧
    for i in col_frames:
        img = cv2.imread(i)
        # 构建一个掩膜
        mask = mask_create()
        # 对原图像进行掩膜计算
        masked_frame = mask_calc(img, mask)
        thresh = threshold(135, 255, masked_frame)
        img = hough(thresh, img)
        cv2.imshow('img', img)
        if cv2.waitKey(40) == ord('q'):
            break
    cv2.destroyAllWindows()


mainn()