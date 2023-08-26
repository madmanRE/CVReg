import cv2
import numpy as np


def compare(image_1, image_2):
    image1 = cv2.imread(image_1)
    image2 = cv2.imread(image_2)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    faces1 = face_cascade.detectMultiScale(
        gray1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    faces2 = face_cascade.detectMultiScale(
        gray2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for x, y, w, h in faces1:
        cv2.rectangle(image1, (x, y), (x + w, y + h), (255, 0, 0), 2)

    for x, y, w, h in faces2:
        cv2.rectangle(image2, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imwrite("tests/1_with_faces.jpg", image1)
    cv2.imwrite("tests/2_with_faces.jpg", image2)

    (x1, y1, w1, h1) = faces1[0]
    (x2, y2, w2, h2) = faces2[0]

    face1_features = gray1[y1 : y1 + h1, x1 : x1 + w1]
    face2_features = gray2[y2 : y2 + h2, x2 : x2 + w2]

    desired_size = (10, 10)
    face1_features = cv2.resize(face1_features, desired_size)
    face2_features = cv2.resize(face2_features, desired_size)

    distance = np.sqrt(np.sum(np.square(face1_features - face2_features)))

    threshold = 100

    print(distance)
    if distance < threshold:
        return True
    else:
        return False
