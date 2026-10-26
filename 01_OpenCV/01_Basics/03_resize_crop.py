import cv2

img = cv2.imread("01_OpenCV/01_Basics/images/test.jpg")

resized = cv2.resize(img, (640, 480))

cropped = img[100:400, 200:600]

cv2.imshow("Original", img)
cv2.imshow("Resized", resized)
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()