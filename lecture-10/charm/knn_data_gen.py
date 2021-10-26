import cv2
import numpy as np
import os

path = "faces.npy"

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

name = input("Enter your name: ")
print(name)
count = 10

data = []

capture = False

while count > 0:

    ret, image = cap.read()
    if ret:
        faces = classifier.detectMultiScale(image, scaleFactor=1.3)

        for face in faces:

            [x, y, w, h] = face

            image = cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 5)
            chopped = image[y:y+h, x:x+w]
            chopped = cv2.resize(chopped, (50, 50))
            gray = cv2.cvtColor(chopped, cv2.COLOR_BGR2GRAY)
            cv2.imshow("My Camera", gray)
            if capture:
                data.append(gray.flatten())
                count -= 1
                print(count, "captures remaining")
                capture = False

        
        
    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    if key == ord("c"):
        capture = True


X = np.array(data)
y = np.array([[name]]*len(data))

print(X.shape, y.shape)

output = np.hstack([X, y])

if os.path.exists(path):
    old = np.load(path)
    output = np.vstack([old, output])

np.save(path, output)









