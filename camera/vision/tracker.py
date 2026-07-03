import math


class TrackerEngine:
    def __init__(self):
        self.next_id = 1
        self.objects = {}
        self.max_distance = 80

    def update(self, detections):
        tracked = []

        for detection in detections:

            x1, y1, x2, y2 = detection["bbox"]

            center = (
                (x1 + x2) // 2,
                (y1 + y2) // 2
            )

            object_id = self._find_existing(center)

            if object_id is None:
                object_id = self.next_id
                self.next_id += 1

            self.objects[object_id] = {
                "center": center,
                "label": detection["name"]
            }

            detection["id"] = object_id

            tracked.append(detection)

        return tracked

    def _find_existing(self, center):

        for object_id, data in self.objects.items():

            old = data["center"]

            distance = math.sqrt(
                (center[0] - old[0]) ** 2 +
                (center[1] - old[1]) ** 2
            )

            if distance < self.max_distance:
                return object_id

        return None