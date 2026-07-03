from ultralytics import YOLO


class ObjectDetector:
    def __init__(self):
        print("Loading YOLO model...")
        self.model = YOLO("yolov8n.pt")
        print("YOLO model loaded.")

    def detect(self, frame):
        return self.model(frame)

    def extract_detections(self, results, min_confidence=0.65):
        detections = []

        for result in results:
            for box in result.boxes:

                confidence = float(box.conf[0])

                # تجاهل النتائج ضعيفة الثقة
                if confidence < min_confidence:
                    continue

                class_id = int(box.cls[0])
                label = result.names[class_id]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detections.append({
                    "name": label,
                    "confidence": round(confidence, 2),
                    "bbox": (x1, y1, x2, y2),
                    "center": (
                        (x1 + x2) // 2,
                        (y1 + y2) // 2
                    )
                })

        return detections