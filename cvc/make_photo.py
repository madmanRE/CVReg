import cv2
import os


def make_profile_photo(filename, id=1):
    face_cascades = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    cap = cv2.VideoCapture(0)

    for i in range(30):
        cap.read()

    ret, frame = cap.read()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascades.detectMultiScale(img_gray)

    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    image_path = f"user_photos_uploads/{filename}/photo{id}.jpg"
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    cv2.imwrite(image_path, frame)
    return image_path


# make_profile_photo()
