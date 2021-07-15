
# 导入需要的包
import numpy as np
import cv2
import sys

def color_transfer(source, target):
  # 将源图像和目标图像从BGR颜色空间转到Lab颜色通道
  # 确保使用OpenCV图像为32位浮点类型数据
  source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
  target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")
  # 计算源图像和目标图像的颜色统计信息(每个通道的均值和标准差)
  # L通道均值、标准差，a通道均值、标准差，b通道均值、标准差
  (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
  (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)
  # 从目标图像中减去均值
  (l, a, b) = cv2.split(target)
  l -= lMeanTar
  a -= aMeanTar
  b -= bMeanTar
  # 按标准差缩放(scale_rate = 目标图像标准差/源图像标准差)
  l = (lStdTar / lStdSrc) * l
  a = (aStdTar / aStdSrc) * a
  b = (bStdTar / bStdSrc) * b
  # 加入源图像对应通道的均值
  l += lMeanSrc
  a += aMeanSrc
  b += bMeanSrc
  # 如果像素强度超出范围，则将像素强度剪裁为[0, 255]范围
  l = np.clip(l, 0, 255)
  a = np.clip(a, 0, 255)
  b = np.clip(b, 0, 255)
  # 将通道合并在一起并转换回BGR颜色空间，确保确保使用 8 位无符号整数数据类型
  transfer = cv2.merge([l, a, b])
  transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)

   # 返回颜色迁移后的图像
  return transfer

def image_stats(image):
   # 计算每个通道的均值和标准差
  (l, a, b) = cv2.split(image)
  (lMean, lStd) = (l.mean(), l.std())
  (aMean, aStd) = (a.mean(), a.std())
  (bMean, bStd) = (b.mean(), b.std())
  # 返回颜色统计信息
  return (lMean, lStd, aMean, aStd, bMean, bStd)

if __name__ == '__main__':
  src = cv2.imread('./0.jpg')
  target = cv2.imread('./2.jpg')
  if src is None or target is None:
    print('图像加载失败，请检查图片路径！')
  else:
    cv2.imshow('src',src)
    cv2.imshow('target', target)
    dst = color_transfer(src, target)
    cv2.imshow('result', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()