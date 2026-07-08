"""
==================================================
OpenEyes Vision OS

Module : Memory Engine
Version: 0.2

Description:
Stores active tracked objects and detects when
objects appear or disappear from the scene.
==================================================
"""


class MemoryEngine:
    def __init__(self):
        self.active_objects = {}

    def remember(self, tracked_objects):
        events = []
        current_ids = set()

        for item in tracked_objects:
            object_id = item.get("id")
            label = item.get("name", "object")
            center = item.get("center")

            if object_id is None:
                continue

            current_ids.add(object_id)

            if object_id not in self.active_objects:
                events.append(f"New object detected: {label} #{object_id}")

            self.active_objects[object_id] = {
                "label": label,
                "center": center,
            }

        previous_ids = set(self.active_objects.keys())
        disappeared_ids = previous_ids - current_ids

        for object_id in disappeared_ids:
            label = self.active_objects[object_id]["label"]
            events.append(f"Object disappeared: {label} #{object_id}")
            del self.active_objects[object_id]

        return events