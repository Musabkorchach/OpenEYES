import cv2

from camera.vision.object_detector import ObjectDetector
from camera.vision.memory import MemoryEngine


class CameraManager:
    def start(self):
        detector = ObjectDetector()
        memory = MemoryEngine()

        cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

        if not cap.isOpened():
            print("Camera not found.")
            return

        print("Camera started with YOLO. Press Q to quit.")

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            results = detector.detect(frame)

            detections = detector.extract_detections(
    results,
    min_confidence=0.65
)
            events = memory.remember(detections)

            for event in events:
                print(event)

            annotated_frame = results[0].plot()

            cv2.imshow("OpenEyes YOLO Object Detection", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()