from datetime import datetime


class MemoryEngine:
    def __init__(self):
        self.seen_objects = {}

    def remember(self, detections):
        events = []
        current_time = datetime.now().strftime("%H:%M:%S")

        for item in detections:
            name = item["name"]
            confidence = item["confidence"]

            if name not in self.seen_objects:
                self.seen_objects[name] = {
                    "first_seen": current_time,
                    "last_seen": current_time,
                    "count": 1,
                    "confidence": confidence,
                }

                events.append(f"New object detected: {name}")

            else:
                self.seen_objects[name]["last_seen"] = current_time
                self.seen_objects[name]["count"] += 1
                self.seen_objects[name]["confidence"] = confidence

        return events

    def summary(self):
        return self.seen_objects