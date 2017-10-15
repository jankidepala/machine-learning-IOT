import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread('k.jpg', cv2.IMREAD_ANYCOLOR)
print(img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()