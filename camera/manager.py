import cv2


class CameraManager:
    def start(self):
        cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

        if not cap.isOpened():
            print("Camera not found.")
            return

        print("Camera started. Press Q to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow("OpenEyes Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()