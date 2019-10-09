# coding=utf-8
# 注意如果脚本中要使用中文，则需要指明编码格式
import cv2
import numpy as np

# imread('图片路径')
img = cv2.imread('wife.jpg')
# 转为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 构造一个sift对象，应该还可以用cv2.xfeatures2d.SURF
sift = cv2.xfeatures2d.SIFT_create()
# 检测出关键点
kp = sift.detect(gray, None)
# 绘制关键点
# cv2.drawKeypoints(image, keypoints[, outImage[, color[, flags]]])
img = cv2.drawKeypoints(gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite('sift_keypoints.jpg', img)
cv2.imshow('sift_keypoints.jpg', img)
