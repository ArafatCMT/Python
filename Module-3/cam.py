import cv2
cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    cv2.imshow("my cam",frame)
    cv2.waitKey(1)