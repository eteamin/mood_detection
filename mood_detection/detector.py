import cv2

from mood_detection.variables import HAARCASCADE_FACE, HAARCASCADE_SMILE


class MoodDetector:
    def __init__(self, face):
        self.face_cascade = cv2.CascadeClassifier(HAARCASCADE_FACE)
        self.smile_cascade = cv2.CascadeClassifier(HAARCASCADE_SMILE)
        self.face = face
        self.image = cv2.imread(face)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def detect(self):

        faces = self.face_cascade.detectMultiScale(self.gray)

        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi_gray = self.gray[y:y + h, x:x + w]
            smile = self.smile_cascade.detectMultiScale(roi_gray)

            if len(smile) > 0:
                return 'Happy!'

            # TODO:  implement other moods
