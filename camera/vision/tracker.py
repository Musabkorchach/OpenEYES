"""
==================================================
OpenEyes Vision OS

Module : Tracker Engine v2
Version: 0.2

Description:
Tracks detected objects across frames using:
- stable IDs
- lost-frame tolerance
- object age
- movement velocity
- distance-based matching
==================================================
"""

import math


class TrackerEngine:
    def __init__(self, max_distance=120, max_lost_frames=15):
        self.next_id = 1
        self.tracks = {}
        self.max_distance = max_distance
        self.max_lost_frames = max_lost_frames

    def update(self, detections):
        tracked_objects = []
        matched_ids = set()

        for detection in detections:
            bbox = detection.get("bbox")

            if bbox is None:
                continue

            label = detection.get("name", "object")
            center = self._center(bbox)

            track_id = self._match(label, center, matched_ids)

            if track_id is None:
                track_id = self._create_track(label, center, bbox)

            else:
                self._update_track(track_id, label, center, bbox)

            matched_ids.add(track_id)

            detection["id"] = track_id
            detection["center"] = center
            detection["velocity"] = self.tracks[track_id]["velocity"]
            detection["age"] = self.tracks[track_id]["age"]

            tracked_objects.append(detection)

        self._mark_lost_tracks(matched_ids)
        self._remove_dead_tracks()

        return tracked_objects

    def _create_track(self, label, center, bbox):
        track_id = self.next_id
        self.next_id += 1

        self.tracks[track_id] = {
            "id": track_id,
            "label": label,
            "center": center,
            "bbox": bbox,
            "age": 1,
            "lost": 0,
            "velocity": (0, 0),
        }

        return track_id

    def _update_track(self, track_id, label, center, bbox):
        old_center = self.tracks[track_id]["center"]

        velocity = (
            center[0] - old_center[0],
            center[1] - old_center[1],
        )

        self.tracks[track_id].update({
            "label": label,
            "center": center,
            "bbox": bbox,
            "age": self.tracks[track_id]["age"] + 1,
            "lost": 0,
            "velocity": velocity,
        })

    def _match(self, label, center, matched_ids):
        best_id = None
        best_distance = self.max_distance

        for track_id, track in self.tracks.items():
            if track_id in matched_ids:
                continue

            if track["label"] != label:
                continue

            distance = self._distance(center, track["center"])

            if distance < best_distance:
                best_distance = distance
                best_id = track_id

        return best_id

    def _mark_lost_tracks(self, matched_ids):
        for track_id in list(self.tracks.keys()):
            if track_id not in matched_ids:
                self.tracks[track_id]["lost"] += 1

    def _remove_dead_tracks(self):
        for track_id in list(self.tracks.keys()):
            if self.tracks[track_id]["lost"] > self.max_lost_frames:
                del self.tracks[track_id]

    def _center(self, bbox):
        x1, y1, x2, y2 = bbox
        return (
            int((x1 + x2) / 2),
            int((y1 + y2) / 2),
        )

    def _distance(self, point_a, point_b):
        return math.sqrt(
            (point_a[0] - point_b[0]) ** 2 +
            (point_a[1] - point_b[1]) ** 2
        )

    def get_tracks(self):
        return self.tracks