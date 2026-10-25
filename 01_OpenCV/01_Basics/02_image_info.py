import cv2

img = cv2.imread("01_OpenCV/01_Basics/images/test.jpg")

print("shape :", img.shape)
print("dtype :", img.dtype)
print("pixel :", img[0, 0])

img[0,0] = [0,0,255]

print("changed pixel :", img[0,0])

img[0:100, 0:100] = [255, 0,0]

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()