import cv2

from camera.vision.object_detector import ObjectDetector
from camera.vision.tracker import TrackerEngine
from camera.vision.memory import MemoryEngine
from camera.vision.scene_analyzer import SceneAnalyzer
from world.world_model import WorldModel
from reasoning.spatial import SpatialReasoningEngine


class CameraManager:
    def start(self):
        detector = ObjectDetector()
        tracker = TrackerEngine()
        memory = MemoryEngine()
        scene_analyzer = SceneAnalyzer()
        world_model = WorldModel()
        spatial_reasoning = SpatialReasoningEngine()

        cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

        if not cap.isOpened():
            print("Camera not found.")
            return

        print("Camera started with OpenEyes Spatial Reasoning. Press Q to quit.")

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Could not read frame.")
                break

            results = detector.detect(frame)
            detections = detector.extract_detections(results)
            tracked_objects = tracker.update(detections)

            world = world_model.update(tracked_objects)
            scene = scene_analyzer.analyze(tracked_objects)
            spatial_insights = spatial_reasoning.analyze(world)
            events = memory.remember(tracked_objects)

            print("Scene:", scene["description"])
            print("World objects:", world["count"])

            for insight in spatial_insights:
                print("Spatial:", insight)

            for event in events:
                print(event)

            annotated_frame = results[0].plot()

            for item in tracked_objects:
                x1, y1, x2, y2 = item["bbox"]
                label = item["name"]
                object_id = item["id"]

                cv2.putText(
                    annotated_frame,
                    f"{label} #{object_id}",
                    (x1, max(20, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2,
                )

            cv2.imshow("OpenEyes Spatial Reasoning", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()