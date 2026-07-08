"""
==================================================
OpenEyes Vision OS

Module : Scene Analyzer
Version : 0.2

Description:
Analyzes the current scene and produces a structured
description of what the camera is observing.

This module is the first step toward scene understanding.
==================================================
"""

from collections import Counter


class SceneAnalyzer:

    def analyze(self, tracked_objects):

        labels = [
            obj["name"]
            for obj in tracked_objects
        ]

        counts = Counter(labels)

        scene = {
            "objects": dict(counts),
            "total_objects": len(tracked_objects),
            "description": self._build_description(counts),
            "people": counts.get("person", 0),
            "chairs": counts.get("chair", 0),
            "tables": counts.get("dining table", 0),
            "screens": counts.get("tv", 0),
        }

        return scene

    def _build_description(self, counts):

        if not counts:
            return "The scene is empty."

        parts = []

        for label, count in counts.items():

            if count == 1:
                parts.append(f"1 {label}")

            else:
                parts.append(f"{count} {label}s")

        return "The scene contains " + ", ".join(parts) + "."