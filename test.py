import numpy as np
import cv2
from numpy.lib.type_check import imag
# the real slim shady

image1 = cv2.imread("test_pics/7.png")


image = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)#将图像转化为灰度图像


#拉普拉斯边缘检测
# lap = cv2.Laplacian(image,cv2.CV_64F)#拉普拉斯边缘检测
canny = cv2.Canny(image, 50, 90)
# cv2.imwrite('canny.png', canny)
cv2.imshow('aa', canny)
cv2.waitKey()
# cv2.imwrite('lap.png', lap)

