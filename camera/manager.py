import cv2


class CameraManager:
    def start(self):
        face_detector = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        eye_detector = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_eye.xml"
        )

        cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

        if not cap.isOpened():
            print("Camera not found.")
            return

        print("Camera started. Press Q to quit.")

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(40, 40)
            )

            for (x, y, w, h) in faces:
                face_roi_gray = gray[y:y + h, x:x + w]
                face_roi_color = frame[y:y + h, x:x + w]

                eyes = eye_detector.detectMultiScale(face_roi_gray)

                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(
                        face_roi_color,
                        (ex, ey),
                        (ex + ew, ey + eh),
                        (255, 0, 0),
                        2
                    )

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    "Face",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

            cv2.putText(
                frame,
                f"Faces: {len(faces)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.imshow("OpenEyes Face And Eye Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()