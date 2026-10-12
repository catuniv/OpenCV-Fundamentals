import cv2
img = cv2.imread("01_OpenCV/01_Basics/images/test.jpg") #이미지 파일 읽어서 img에 저장

cv2.imshow("Image", img) #img를 화면에 띄움

cv2.waitKey(0) # 키보드 입력이 들어올 때까지 기다림
cv2.destroyAllWindows() #OpenCV 창을 모두 닫음