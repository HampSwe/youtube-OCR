import cv2
import pytesseract
import time

imPath = './test_images/rotated2.png'
im = cv2.imread(imPath)

cv2.imshow("hello", im)
cv2.waitKey(0)

newdata = pytesseract.image_to_osd(imPath)

print(newdata)