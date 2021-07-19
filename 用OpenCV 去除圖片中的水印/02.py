import cv2
import numpy as np

if __name__ =='__main__':
    img_path = "F:/Data/Ceshi1/shuiyin.jpg"
    im = cv2.imread(img_path)

    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    background = gray.copy()
    for i in range(1,5):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*i+1,2*i+1))
        # print('kernel size is ',kernel)
        background = cv2.morphologyEx(background,cv2.MORPH_CLOSE,kernel)
        background = cv2.morphologyEx(background,cv2.MORPH_CLOSE,kernel)

    diff = background - gray # 计算差距

    cv2.namedWindow('diff',cv2.WINDOW_FREERATIO) # 获取图像中前景背景之差
    cv2.imshow('diff',background)
    # 阈值分割获取黑色字体
    _,bw = cv2.threshold(diff,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # 阈值分割获取黑色区域
    cv2.namedWindow('bw_before', cv2.WINDOW_FREERATIO)
    cv2.imshow('bw_before', bw)


    _,dark = cv2.threshold(background,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

    darkpix = cv2.countNonZero(dark)# 获取 dark非0d图像像素个数
    darkpix = [0]*darkpix
    index = 0
    cv2.namedWindow('gray', cv2.WINDOW_FREERATIO)
    cv2.imshow('gray', gray)



    for r in range(dark.shape[0]):
        for c in range(dark.shape[1]):
            if(dark[r][c]):
                darkpix[index]  = gray[r][c]
                index = index +1

    # 阈值分割 dark 区域 因此我们在里面得到更深的像素
    darkpix = np.array(darkpix)
    _,darkpix = cv2.threshold(darkpix,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.namedWindow('darkpix', cv2.WINDOW_FREERATIO)
    cv2.imshow('darkpix', darkpix)

    # 把 取到的像素粘贴到 其渠道的 darker pixels

    cv2.namedWindow('dark',cv2.WINDOW_FREERATIO)
    cv2.imshow('dark',dark)

    index = 0
    for r in range(dark.shape[0]):
        for c in range(dark.shape[1]):
            if (dark[r][c]):
                bw[r][c] =  darkpix[index]
                index = index +1

    cv2.namedWindow('bw',cv2.WINDOW_FREERATIO)
    cv2.imshow('bw',bw)
    cv2.waitKey(0)