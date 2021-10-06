import cv2

cap = cv2.VideoCapture(1)

while True:

    ret, image = cap.read()

    if ret:
        cv2.imshow("My Camera", image)

    key = cv2.waitKey(50)

    if key == ord("q"):
        break
    if key == ord("c"):
        cv2.imwrite("classroom.png", image)




