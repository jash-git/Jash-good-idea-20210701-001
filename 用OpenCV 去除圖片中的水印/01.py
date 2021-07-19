import cv2
import numpy as np

if __name__ =='__main__':
    img_path = "F:/Data/Ceshi1/shuiyin.jpg"

    img1 = cv2.imread(img_path)
    cv2.namedWindow('img1',cv2.WINDOW_FREERATIO)
    cv2.imshow('img1',img1)

    # 转化为 灰度图
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    # 创建一个白画布
    ellipse_img = np.full((img1.shape[0],img1.shape[1],3),0,dtype = np.uint8)
    print(ellipse_img.shape,ellipse_img[0][0])
    gray = cv2.GaussianBlur(gray,(5,5),0) # 高斯处理
    # 应用霍夫圆检测,检测出所有圆
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,gray.shape[0]/8,100,100,100,0)


    # 找到最大的圆
    measure = 0.0
    x = 0.0
    y = 0.0
    for circle in (circles[0]):
        if circle[2] > measure:
            measure = circle[2]
            x = circle[0]
            y = circle[1]

    # 绘制圆
    cv2.circle(img1,(x,y),3,(0,255,0),-1,8,0)
    cv2.circle(img1,(x,y),int(measure),(0,255,0),2,8,0)
    # 绘制相同大小的圆
    ellipse_img =  cv2.ellipse(ellipse_img,(x,y),(int(measure),int(measure)),0,0,360,(255,255,255),-1,8)
    print(f'center x is {x} ,y is {y}, radius is {measure}')
    ellipse_img = cv2.cvtColor(ellipse_img,cv2.COLOR_BGR2GRAY)

    result = cv2.bitwise_and(gray,ellipse_img)


    cv2.namedWindow('bitwise and',cv2.WINDOW_FREERATIO)
    cv2.imshow('bitwise and',result)

    # 估计圆图像像素强度
    x = result[int(x+30)][int(y)]
    print(f'intensity is  {x}')


    # 阈值分割
    _,ellipse_img = cv2.threshold(result,int(x) - 10,250,cv2.THRESH_BINARY)
    # print('ellipse_img shape is {}'.format(ellipse_img.shape))
    cv2.namedWindow('threshold',cv2.WINDOW_FREERATIO)
    cv2.imshow('threshold',ellipse_img)

    # 使用 bitwise_or 方法
    print('shape ------------\n')
    print(ellipse_img.shape,gray.shape)
    res = cv2.bitwise_or(gray,ellipse_img)

    cv2.namedWindow('bitwise_or',cv2.WINDOW_FREERATIO)
    cv2.imshow('bitwise_or',res)

    cv2.waitKey(0)
