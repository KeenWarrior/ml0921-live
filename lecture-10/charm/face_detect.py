import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier

path = "faces.npy"

data = np.load(path)

X = data[:, :-1].astype(int)
y = data[:, -1]

model = KNeighborsClassifier(4)
model.fit(X, y)

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

while True:

    ret, image = cap.read()
    if ret:
        faces = classifier.detectMultiScale(image, scaleFactor=1.3)

        for face in faces:

            [x, y, w, h] = face

            image = cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 5)

            chopped = image[y:y+h, x:x+w]
            chopped = cv2.resize(chopped, (100, 100))
            gray = cv2.cvtColor(chopped, cv2.COLOR_BGR2GRAY)
            names = model.predict([gray.flatten()])

            cv2.putText(image, names[0],
                        (x, y-20),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 255, 0),
                        4)

        cv2.imshow("Predictor", image)

    key = cv2.waitKey(10)

    if key == ord("q"):
        break


